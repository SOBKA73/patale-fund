from __future__ import annotations

from dataclasses import dataclass, replace
from decimal import Decimal
from typing import Any

from .models import AgentDecision, MarketContext, Proposal
from .roles import QuantResearcherAgent, RiskManagerAgent


@dataclass(frozen=True)
class DebatePolicy:
    max_rounds: int = 2
    risk_veto: bool = True
    allow_size_reduction: bool = True

    def validate(self) -> "DebatePolicy":
        if self.max_rounds not in (1, 2, 3):
            raise ValueError("debate.max_rounds doit être 1, 2 ou 3")
        return self


@dataclass(frozen=True)
class DebateTurn:
    round_number: int
    speaker: str
    message_type: str
    content: str
    evidence: dict[str, Any]


@dataclass(frozen=True)
class DebateResult:
    status: str
    final_decision: AgentDecision
    turns: tuple[DebateTurn, ...]


class QuantRiskDebate:
    """Débat déterministe préalable à toute sélection d’ordre simulé."""

    def __init__(self, quant: QuantResearcherAgent, risk: RiskManagerAgent, policy: DebatePolicy | None = None):
        self.quant = quant
        self.risk = risk
        self.policy = (policy or DebatePolicy()).validate()

    def run(self, proposal: Proposal, context: MarketContext) -> DebateResult:
        turns: list[DebateTurn] = [
            DebateTurn(1, proposal.agent.name, "PROPOSAL", proposal.rationale, proposal.evidence)
        ]
        decision = self.risk.review(proposal, context)
        if decision.status == "APPROVED":
            turns.append(DebateTurn(1, self.risk.identity.name, "RISK_APPROVAL", decision.reason, {}))
            return DebateResult("APPROVED", decision, tuple(turns))

        turns.append(
            DebateTurn(
                1, self.risk.identity.name, "RISK_OBJECTION", decision.reason, {"constraints": decision.constraints}
            )
        )
        if self.policy.max_rounds < 2 or not self.policy.allow_size_reduction:
            return DebateResult("VETOED", decision, tuple(turns))

        rebuttal = self._rebut(proposal, decision)
        turns.append(DebateTurn(2, rebuttal.agent.name, "REBUTTAL", rebuttal.rationale, rebuttal.evidence))
        final = self.risk.review(rebuttal, context)
        if final.status == "APPROVED":
            turns.append(DebateTurn(2, self.risk.identity.name, "RISK_APPROVAL", final.reason, {}))
            return DebateResult("APPROVED_AFTER_REBUTTAL", final, tuple(turns))

        turns.append(
            DebateTurn(2, self.risk.identity.name, "RISK_VETO", final.reason, {"constraints": final.constraints})
        )
        status = "VETOED" if self.policy.risk_veto else "ESCALATED"
        return DebateResult(status, final, tuple(turns))

    @staticmethod
    def _rebut(proposal: Proposal, objection: AgentDecision) -> Proposal:
        reduced = proposal.target_weight / Decimal("2")
        return replace(
            proposal,
            target_weight=reduced,
            rationale=(
                "réponse Quant : taille réduite de moitié après objection Risk ; " "aucune nouvelle donnée non vérifiée"
            ),
            evidence={**proposal.evidence, "risk_objection": objection.reason, "size_reduced": True},
        )
