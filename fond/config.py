from __future__ import annotations

import os
import tomllib
from dataclasses import dataclass
from pathlib import Path

PAPER_URL = "https://paper-api.alpaca.markets"


@dataclass(frozen=True)
class StrategyConfig:
    window: int = 20
    entry_z: float = -2.0
    exit_z: float = 0.0


@dataclass(frozen=True)
class RiskConfig:
    max_position_pct: float = 0.05
    max_daily_loss_pct: float = 0.02
    max_leverage: float = 1.0


@dataclass(frozen=True)
class BacktestConfig:
    initial_capital: float = 100_000.0
    commission_per_trade: float = 0.0
    slippage_bps: float = 5.0


@dataclass(frozen=True)
class ExecutionConfig:
    base_url: str = PAPER_URL
    dry_run: bool = True


@dataclass(frozen=True)
class AppConfig:
    strategy: StrategyConfig = StrategyConfig()
    risk: RiskConfig = RiskConfig()
    backtest: BacktestConfig = BacktestConfig()
    execution: ExecutionConfig = ExecutionConfig()

    def validate(self) -> "AppConfig":
        s, r, b, e = self.strategy, self.risk, self.backtest, self.execution
        if not 2 <= s.window <= 10_000:
            raise ValueError("strategy.window doit être entre 2 et 10000")
        if s.entry_z >= s.exit_z:
            raise ValueError("strategy.entry_z doit être inférieur à strategy.exit_z")
        if not 0 < r.max_position_pct <= 1:
            raise ValueError("risk.max_position_pct invalide")
        if not 0 < r.max_daily_loss_pct <= 1:
            raise ValueError("risk.max_daily_loss_pct invalide")
        if not 0 < r.max_leverage <= 10:
            raise ValueError("risk.max_leverage invalide")
        if b.initial_capital <= 0 or b.commission_per_trade < 0 or b.slippage_bps < 0:
            raise ValueError("paramètres backtest invalides")
        if e.base_url != PAPER_URL:
            raise ValueError(f"execution.base_url doit être exactement {PAPER_URL}")
        return self


def load_config(path: str | Path = "config.toml") -> AppConfig:
    raw = {}
    if Path(path).exists():
        with Path(path).open("rb") as f:
            raw = tomllib.load(f)
    return AppConfig(
        StrategyConfig(**raw.get("strategy", {})),
        RiskConfig(**raw.get("risk", {})),
        BacktestConfig(**raw.get("backtest", {})),
        ExecutionConfig(**raw.get("execution", {})),
    ).validate()


def paper_credentials() -> tuple[str, str]:
    key, secret = os.getenv("ALPACA_API_KEY"), os.getenv("ALPACA_SECRET_KEY")
    if not key or not secret:
        raise RuntimeError("ALPACA_API_KEY et ALPACA_SECRET_KEY sont requis pour l'envoi paper")
    return key, secret
