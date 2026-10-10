from __future__ import annotations

import argparse

from .audit import append_event
from .backtest import run
from .config import load_config
from .data import load_prices
from .execution import PaperExecutor


def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="command", required=True)
    for name in ("backtest", "paper"):
        cmd = sub.add_parser(name)
        cmd.add_argument("--data", required=True)
        cmd.add_argument("--config", default="config.toml")
        if name == "paper":
            cmd.add_argument("--send-paper-orders", action="store_true")
    a = p.parse_args()
    config = load_config(a.config)
    prices = load_prices(a.data)
    if a.command == "backtest":
        result = run(prices, config)
        append_event("logs/audit.jsonl", "DECISION", result["metrics"])
        print(result["metrics"])
        return 0
    PaperExecutor(config, send_paper_orders=a.send_paper_orders)
    print("paper mode: no orders sent without explicit valid configuration")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
