from __future__ import annotations

from pathlib import Path

import pandas as pd

COLUMNS = ["date", "open", "high", "low", "close", "volume"]


def load_prices(path: str | Path) -> pd.DataFrame:
    frame = pd.read_csv(path)
    missing = set(COLUMNS) - set(frame.columns)
    if missing:
        raise ValueError(f"colonnes manquantes: {sorted(missing)}")
    frame = frame[COLUMNS].copy()
    frame["date"] = pd.to_datetime(frame["date"], errors="raise", utc=True)
    if frame["date"].duplicated().any():
        raise ValueError("dates dupliquées")
    if not frame["date"].is_monotonic_increasing:
        raise ValueError("dates non chronologiques")
    if frame["close"].isna().any():
        raise ValueError("close contient des valeurs manquantes")
    for col in COLUMNS[1:]:
        frame[col] = pd.to_numeric(frame[col], errors="raise")
    if (frame["close"] <= 0).any():
        raise ValueError("close doit être positif")
    return frame


def returns(prices: pd.DataFrame) -> pd.Series:
    return prices["close"].pct_change().fillna(0.0)
