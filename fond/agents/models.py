from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any

import pandas as pd


@dataclass(frozen=True)
class AgentIdentity:
    name: str
    role: str
    autonomy: str = "simulated"


@dataclass(frozen=True)
class MarketContext:
    prices: pd.DataFrame
    capital: Decimal
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class Proposal:
    agent: AgentIdentity
    kind: str
    symbol: str
    action: str
    target_weight: Decimal
    confidence: float
    rationale: str
    evidence: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class AgentDecision:
    agent: AgentIdentity
    status: str
    reason: str
    proposal: Proposal | None = None
    constraints: tuple[str, ...] = ()
