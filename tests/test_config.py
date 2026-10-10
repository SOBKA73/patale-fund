import pytest

from fond.config import PAPER_URL, AppConfig, ExecutionConfig, StrategyConfig, load_config


def test_defaults_are_safe():
    c = load_config("missing.toml")
    assert c.execution.dry_run and c.execution.base_url == PAPER_URL


def test_live_url_rejected():
    with pytest.raises(ValueError):
        AppConfig(execution=ExecutionConfig(base_url="https://api.alpaca.markets")).validate()


def test_invalid_bounds_rejected():
    with pytest.raises(ValueError):
        AppConfig(strategy=StrategyConfig(window=1)).validate()
