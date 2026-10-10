import pandas as pd

from fond.metrics import calculate


def test_empty_and_constant_cases():
    assert calculate(pd.Series(dtype=float), [])["trade_count"] == 0
    assert calculate(pd.Series([100, 100]), [])["sharpe"] is None
