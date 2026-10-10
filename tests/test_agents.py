from decimal import Decimal

import pandas as pd

from fond.agents.models import AgentIdentity
from fond.agents.orchestrator import AutonomousSimulation
from fond.agents.registry import AgentRegistry
from fond.config import load_config


def prices() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "date": pd.date_range("2024-01-01", periods=25),
            "open": [100.0] * 25,
            "high": [101.0] * 25,
            "low": [99.0] * 25,
            "close": [100.0] * 25,
            "volume": [1000] * 25,
        }
    )


def test_registry_rejects_duplicate_agents():
    registry = AgentRegistry()
    from fond.agents.roles import DataAgent

    registry.register(DataAgent(AgentIdentity("data", "Data Engineer")))
    try:
        registry.register(DataAgent(AgentIdentity("data", "Data Engineer")))
    except ValueError:
        return
    assert False


def test_cycle_bootstraps_one_billion_axe_and_stays_external_order_free():
    simulation = AutonomousSimulation(load_config(), prices())
    first = simulation.run_cycle()
    second = simulation.run_cycle()
    assert first["capital_axe"]["name"] == "Axe Coin"
    assert first["capital_axe"]["symbol"] == "AXE"
    assert Decimal(first["capital_axe"]["outstanding"]) == Decimal("1000000000")
    assert first["external_orders"] == second["external_orders"] == 0
    assert first["portfolio_decision"].status in {"SELECTED", "ESCALATED"}
