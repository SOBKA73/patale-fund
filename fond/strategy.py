from __future__ import annotations

import pandas as pd

from .config import StrategyConfig


def signals(prices: pd.DataFrame, config: StrategyConfig) -> pd.Series:
    close = prices["close"].astype(float)
    mean = close.rolling(config.window, min_periods=config.window).mean()
    std = close.rolling(config.window, min_periods=config.window).std(ddof=0)
    z = (close - mean).div(std.where(std != 0))
    out, position = [], 0
    for value in z:
        if position == 0 and pd.notna(value) and value <= config.entry_z:
            position = 1
        elif position == 1 and pd.notna(value) and value >= config.exit_z:
            position = 0
        out.append(position)
    return pd.Series(out, index=prices.index, name="signal", dtype=int)
