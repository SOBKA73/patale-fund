from __future__ import annotations

import math

import pandas as pd


def calculate(equity: pd.Series, trades: list[dict], risk_free_rate: float = 0.0) -> dict:
    e = equity.astype(float)
    if e.empty:
        return {
            "total_return": None,
            "annualized_return": None,
            "annualized_volatility": None,
            "sharpe": None,
            "max_drawdown": None,
            "trade_count": 0,
            "win_rate": None,
        }
    total = e.iloc[-1] / e.iloc[0] - 1
    n = len(e)
    annual = (1 + total) ** (252 / max(n - 1, 1)) - 1 if e.iloc[0] > 0 else None
    daily = e.pct_change().dropna()
    vol = daily.std(ddof=1) * math.sqrt(252) if len(daily) > 1 else None
    excess = daily - risk_free_rate / 252
    sharpe = excess.mean() / daily.std(ddof=1) * math.sqrt(252) if len(daily) > 1 and daily.std(ddof=1) != 0 else None
    drawdown = e / e.cummax() - 1
    pnls = [float(t["pnl"]) for t in trades]
    return {
        "total_return": float(total),
        "annualized_return": annual,
        "annualized_volatility": None if vol is None else float(vol),
        "sharpe": None if sharpe is None else float(sharpe),
        "max_drawdown": float(drawdown.min()),
        "trade_count": len(trades),
        "win_rate": None if not pnls else sum(p > 0 for p in pnls) / len(pnls),
    }
