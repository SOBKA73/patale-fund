import pandas as pd

from fond.config import StrategyConfig
from fond.strategy import signals


def test_signals_stable_for_prior_history():
    p = pd.DataFrame({"close": [10, 10, 10, 10, 8, 10, 10, 10]})
    c = StrategyConfig(window=3, entry_z=-1, exit_z=0)
    a = signals(p, c)
    q = p.copy()
    q.loc[7, "close"] = 1000
    assert a.iloc[:7].equals(signals(q, c).iloc[:7])
