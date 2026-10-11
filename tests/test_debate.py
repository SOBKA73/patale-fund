from decimal import Decimal

import pandas as pd

from fond.agents.debate import DebatePolicy, QuantRiskDebate
from fond.agents.models import MarketContext, Proposal
from fond.agents.roles import QuantResearcherAgent, RiskManagerAgent
from fond.config import AppConfig, RiskConfig, load_config


def context(capital: str = "1000000") -> MarketContext:
    prices = pd.DataFrame({"date": pd.date_range("2024-01-01", periods=3), "close": [100.0, 100.0, 100.0]})
    return MarketContext(prices, Decimal(capital))


def test_risk_veto_blocks_oversized_proposal_after_rebuttal():
    config = AppConfig(risk=RiskConfig(max_position_pct=0.01, max_leverage=1.0))
    quant, risk = QuantResearcherAgent(config), RiskManagerAgent(config)
    proposal = Proposal(quant.identity, "ORDER_PROPOSAL", "SIM", "BUY", Decimal("2.0"), 0.9, "test", {})
    result = QuantRiskDebate(quant, risk).run(proposal, context())
    assert result.status == "VETOED"
    assert result.final_decision.status == "REJECTED"
    assert [turn.message_type for turn in result.turns] == ["PROPOSAL", "RISK_OBJECTION", "REBUTTAL", "RISK_VETO"]


def test_approved_order_requires_explicit_risk_approval():
    config = load_config()
    quant, risk = QuantResearcherAgent(config), RiskManagerAgent(config)
    proposal = Proposal(quant.identity, "ORDER_PROPOSAL", "SIM", "BUY", Decimal("0.01"), 0.8, "test", {})
    result = QuantRiskDebate(quant, risk, DebatePolicy(max_rounds=2)).run(proposal, context("1000000000"))
    assert result.status == "APPROVED"
    assert result.final_decision.agent.name == "risk-manager-01"
    assert result.turns[-1].message_type == "RISK_APPROVAL"
