from __future__ import annotations

from typing import Any

from ..config import AppConfig
from ..token import TokenLedger
from .models import AgentIdentity, MarketContext
from .registry import AgentRegistry
from .roles import DataAgent, PortfolioManagerAgent, QuantResearcherAgent, RiskManagerAgent


class AutonomousSimulation:
    """Cycle local : observation, recherche, contrôle risque et sélection de portefeuille."""

    def __init__(self, config: AppConfig, prices, ledger: TokenLedger | None = None) -> None:
        self.config = config.validate()
        self.prices = prices
        self.ledger = ledger or TokenLedger(self.config.token)
        self.registry = AgentRegistry()
        self.data = DataAgent(AgentIdentity("data-engineer-01", "Data Engineer"))
        self.quant = QuantResearcherAgent(self.config)
        self.risk = RiskManagerAgent(self.config)
        self.portfolio = PortfolioManagerAgent()
        for agent in (self.data, self.quant, self.risk, self.portfolio):
            self.registry.register(agent)
        self._bootstrap_capital()

    def _bootstrap_capital(self) -> None:
        account = self.portfolio.identity.name
        if self.ledger.outstanding == 0:
            self.ledger.issue(account, self.config.token.max_supply, self.config.token.issuer_account)

    def run_cycle(self) -> dict[str, Any]:
        context = MarketContext(
            self.prices, self.ledger.balance_of(self.portfolio.identity.name), {"mode": "simulation"}
        )
        data_report = self.data.act(context)
        proposal = self.quant.act(context)
        risk_decision = self.risk.review(proposal, context)
        portfolio_decision = self.portfolio.select([risk_decision], context)
        return {
            "mode": "simulation_only",
            "autonomy": "bounded_and_auditable",
            "data_report": data_report,
            "proposal": proposal,
            "risk_decision": risk_decision,
            "portfolio_decision": portfolio_decision,
            "capital_axe": self.ledger.snapshot(),
            "external_orders": 0,
        }
