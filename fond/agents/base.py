from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from .models import AgentIdentity, MarketContext


class SimulatedAgent(ABC):
    """Agent autonome dans le périmètre de la simulation, jamais conscient au sens réel."""

    def __init__(self, identity: AgentIdentity) -> None:
        self.identity = identity
        self.state: dict[str, Any] = {"cycle_count": 0}

    @abstractmethod
    def act(self, context: MarketContext) -> Any:
        """Agit localement et retourne une sortie structurée et auditable."""

    def observe(self, context: MarketContext) -> None:
        self.state["cycle_count"] += 1
        self.state["observations"] = len(context.prices)
