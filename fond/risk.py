from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from .config import RiskConfig


@dataclass(frozen=True)
class Decision:
    allowed: bool
    reason: str


class DailyLossCircuitBreaker:
    def __init__(self, config: RiskConfig):
        self.config, self.day, self.blocked = config, None, False

    def check(self, current_day: date, equity_start: float, equity_now: float) -> Decision:
        if self.day != current_day:
            self.day, self.blocked = current_day, False
        loss = max(0.0, (equity_start - equity_now) / equity_start) if equity_start else 1.0
        if loss >= self.config.max_daily_loss_pct:
            self.blocked = True
        return Decision(not self.blocked, "daily_loss_limit" if self.blocked else "allowed")


def check_position(equity: float, quantity: int, price: float, config: RiskConfig) -> Decision:
    if equity <= 0 or quantity < 0 or quantity * price > equity * config.max_position_pct:
        return Decision(False, "position_limit")
    return Decision(True, "allowed")


def check_leverage(equity: float, gross_exposure: float, config: RiskConfig) -> Decision:
    if equity <= 0 or gross_exposure > equity * config.max_leverage:
        return Decision(False, "leverage_limit")
    return Decision(True, "allowed")
