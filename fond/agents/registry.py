from __future__ import annotations

from .base import SimulatedAgent


class AgentRegistry:
    def __init__(self) -> None:
        self._agents: dict[str, SimulatedAgent] = {}

    def register(self, agent: SimulatedAgent) -> None:
        if agent.identity.name in self._agents:
            raise ValueError(f"agent déjà enregistré: {agent.identity.name}")
        self._agents[agent.identity.name] = agent

    def get(self, name: str) -> SimulatedAgent:
        return self._agents[name]

    def all(self) -> tuple[SimulatedAgent, ...]:
        return tuple(self._agents.values())
