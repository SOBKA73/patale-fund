from datetime import date

from fond.config import RiskConfig
from fond.risk import DailyLossCircuitBreaker, check_leverage, check_position


def test_position_and_leverage_limits():
    c = RiskConfig(max_position_pct=0.05, max_leverage=1)
    assert check_position(100, 5, 1, c).allowed and not check_position(100, 6, 1, c).allowed
    assert check_leverage(100, 100, c).allowed and not check_leverage(100, 101, c).allowed


def test_circuit_breaker_resets_only_on_date_change():
    b = DailyLossCircuitBreaker(RiskConfig(max_daily_loss_pct=0.02))
    d = date(2024, 1, 1)
    assert not b.check(d, 100, 97.9).allowed
    assert not b.check(d, 100, 99).allowed
    assert b.check(date(2024, 1, 2), 100, 99).allowed
