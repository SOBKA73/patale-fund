import pandas as pd

from fond.backtest import run
from fond.config import AppConfig, BacktestConfig


def prices():
    return pd.DataFrame(
        {
            "date": pd.date_range("2024-01-01", periods=8),
            "open": [10] * 8,
            "high": [10] * 8,
            "low": [10] * 8,
            "close": [10, 10, 10, 8, 10, 10, 10, 10],
            "volume": [1] * 8,
        }
    )


def test_deterministic_and_capital():
    c = AppConfig(backtest=BacktestConfig(initial_capital=1000))
    a, b = run(prices(), c), run(prices(), c)
    assert a["equity"].equals(b["equity"]) and a["equity"].iloc[0] == 1000
