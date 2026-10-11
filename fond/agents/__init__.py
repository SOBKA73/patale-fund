"""Agents autonomes simulés, déterministes et soumis aux garde-fous du moteur."""

from .debate import DebatePolicy, QuantRiskDebate
from .orchestrator import AutonomousSimulation
from .registry import AgentRegistry
from .roles import DataAgent, PortfolioManagerAgent, QuantResearcherAgent, RiskManagerAgent

__all__ = [
    "AgentRegistry",
    "AutonomousSimulation",
    "DebatePolicy",
    "QuantRiskDebate",
    "DataAgent",
    "PortfolioManagerAgent",
    "QuantResearcherAgent",
    "RiskManagerAgent",
]
