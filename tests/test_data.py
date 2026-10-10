import pandas as pd
import pytest

from fond.data import load_prices, returns


def frame():
    return pd.DataFrame(
        {
            "date": ["2024-01-01", "2024-01-02"],
            "open": [1, 1],
            "high": [1, 1],
            "low": [1, 1],
            "close": [1, 2],
            "volume": [1, 2],
        }
    )


def test_load_prices(tmp_path):
    p = tmp_path / "p.csv"
    frame().to_csv(p, index=False)
    assert len(load_prices(p)) == 2
    assert returns(load_prices(p)).iloc[-1] == 1


def test_missing_column_rejected(tmp_path):
    p = tmp_path / "p.csv"
    frame().drop(columns=["close"]).to_csv(p, index=False)
    with pytest.raises(ValueError):
        load_prices(p)


def test_duplicate_dates_rejected(tmp_path):
    p = tmp_path / "p.csv"
    x = frame()
    x.loc[1, "date"] = x.loc[0, "date"]
    x.to_csv(p, index=False)
    with pytest.raises(ValueError):
        load_prices(p)
