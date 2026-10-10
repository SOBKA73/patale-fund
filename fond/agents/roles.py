from __future__ import annotations

from decimal import Decimal

from ..config import AppConfig
from ..risk import check_leverage, check_position
from ..strategy import signals
from .base import SimulatedAgent
from .models import AgentDecision, AgentIdentity, MarketContext, Proposal


class DataAgent(SimulatedAgent):
    def act(self, context: MarketContext) -> dict:
        if context.prices.empty:
            raise ValueError("l'agent data refuse un jeu de données vide")
        required = {"date", "close"}
        if not required.issubset(context.prices.columns):
            raise ValueError("l'agent data refuse des colonnes insuffisantes")
        self.observe(context)
        return {
            "agent": self.identity.name,
            "rows": len(context.prices),
            "last_close": float(context.prices["close"].iloc[-1]),
        }


class QuantResearcherAgent(SimulatedAgent):
    def __init__(self, config: AppConfig) -> None:
        super().__init__(AgentIdentity("quant-researcher-01", "Quant Researcher"))
        self.config = config

    def act(self, context: MarketContext) -> Proposal:
        self.observe(context)
        signal = int(signals(context.prices, self.config.strategy).iloc[-1])
        action = "BUY" if signal == 1 else "HOLD"
        return Proposal(
            agent=self.identity,
            kind="STRATEGY_PROPOSAL",
            symbol="SIM",
            action=action,
            target_weight=Decimal(str(self.config.risk.max_position_pct if signal else 0)),
            confidence=0.60 if signal else 0.50,
            rationale="signal z-score long-only ; aucune donnée future utilisée",
            evidence={"signal": signal, "rows": len(context.prices)},
        )


class RiskManagerAgent(SimulatedAgent):
    def __init__(self, config: AppConfig) -> None:
        super().__init__(AgentIdentity("risk-manager-01", "Risk Manager"))
        self.config = config

    def act(self, context: MarketContext) -> dict:
        self.observe(context)
        return {"agent": self.identity.name, "status": "ready", "limits": self.config.risk}

    def review(self, proposal: Proposal, context: MarketContext) -> AgentDecision:
        self.observe(context)
        price = float(context.prices["close"].iloc[-1])
        quantity = int((context.capital * proposal.target_weight) // Decimal(str(price)))
        position = check_position(float(context.capital), quantity, price, self.config.risk)
        leverage = check_leverage(float(context.capital), quantity * price, self.config.risk)
        if not position.allowed or not leverage.allowed:
            return AgentDecision(
                self.identity,
                "REJECTED",
                f"risk refusal: {position.reason}/{leverage.reason}",
                proposal,
                (position.reason, leverage.reason),
            )
        return AgentDecision(self.identity, "APPROVED", "position et levier dans les limites", proposal)


class PortfolioManagerAgent(SimulatedAgent):
    def __init__(self) -> None:
        super().__init__(AgentIdentity("portfolio-manager-01", "Portfolio Manager"))

    def act(self, context: MarketContext) -> dict:
        self.observe(context)
        return {"agent": self.identity.name, "status": "ready", "capital": str(context.capital)}

    def select(self, decisions: list[AgentDecision], context: MarketContext) -> AgentDecision:
        self.observe(context)
        approved = [decision for decision in decisions if decision.status == "APPROVED" and decision.proposal]
        if not approved:
            return AgentDecision(
                self.identity, "ESCALATED", "aucune proposition approuvée", None, ("human_review_available",)
            )
        selected = max(approved, key=lambda item: item.proposal.confidence)
        return AgentDecision(self.identity, "SELECTED", "proposition approuvée sélectionnée", selected.proposal)
