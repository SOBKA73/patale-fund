from __future__ import annotations

import pandas as pd

from .config import AppConfig
from .metrics import calculate
from .strategy import signals


def run(prices: pd.DataFrame, config: AppConfig) -> dict:
    config.validate()
    sig = signals(prices, config.strategy)
    cash, shares, entry = config.backtest.initial_capital, 0, None
    equity, trades = [], []
    slip = config.backtest.slippage_bps / 10_000
    for i, row in prices.iterrows():
        price = float(row.close)
        if i > 0:
            prev = int(sig.iloc[i - 1])
            if shares == 0 and prev == 1:
                qty = int((cash * config.risk.max_position_pct) // price)
                if qty:
                    cash -= qty * price * (1 + slip) + config.backtest.commission_per_trade
                    shares, entry = qty, price * (1 + slip)
            elif shares and prev == 0:
                exit_price = price * (1 - slip)
                proceeds = shares * exit_price - config.backtest.commission_per_trade
                pnl = proceeds - shares * entry - config.backtest.commission_per_trade
                trades.append(
                    {
                        "entry_date": str(prices.iloc[i - 1].date),
                        "exit_date": str(row.date),
                        "entry_price": entry,
                        "exit_price": exit_price,
                        "quantity": shares,
                        "pnl": pnl,
                    }
                )
                cash += proceeds
                shares, entry = 0, None
        equity.append(cash + shares * price)
    return {
        "equity": pd.Series(equity, index=prices.index, name="equity"),
        "trades": trades,
        "metrics": calculate(pd.Series(equity), trades),
    }
