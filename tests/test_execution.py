from fond.config import AppConfig, ExecutionConfig
from fond.execution import PaperExecutor


def test_dry_run_writes_no_network(tmp_path):
    executor = PaperExecutor(AppConfig(), str(tmp_path / "audit.jsonl"), False)
    result = executor.submit_market_order("TEST", 1, "buy", 10)
    assert result["status"] == "DRY_RUN" and executor.client is None


def test_live_url_rejected():
    try:
        PaperExecutor(AppConfig(execution=ExecutionConfig(base_url="https://api.alpaca.markets")))
    except ValueError:
        return
    assert False


def test_paper_order_is_sent_only_with_explicit_configuration(monkeypatch, tmp_path):
    class FakeOrder:
        id = "paper-order-id"

    class FakeClient:
        def __init__(self, *args, **kwargs):
            assert kwargs["paper"] is True

        def submit_order(self, request):
            return FakeOrder()

    monkeypatch.setattr("fond.execution.paper_credentials", lambda: ("key", "secret"))
    monkeypatch.setattr("alpaca.trading.client.TradingClient", FakeClient)
    config = AppConfig(execution=ExecutionConfig(dry_run=False))
    executor = PaperExecutor(config, str(tmp_path / "audit.jsonl"), True)
    result = executor.submit_market_order("TEST", 1, "sell", 10)
    assert result["status"] == "ORDER_SENT"


def test_invalid_order_rejected(tmp_path):
    executor = PaperExecutor(AppConfig(), str(tmp_path / "audit.jsonl"), False)
    try:
        executor.submit_market_order("TEST", 0, "buy", 10)
    except ValueError:
        return
    assert False


def test_network_error_is_audited(monkeypatch, tmp_path):
    class FailingClient:
        def __init__(self, *args, **kwargs):
            pass

        def submit_order(self, request):
            raise RuntimeError("network disabled in test")

    monkeypatch.setattr("fond.execution.paper_credentials", lambda: ("key", "secret"))
    monkeypatch.setattr("alpaca.trading.client.TradingClient", FailingClient)
    audit = tmp_path / "audit.jsonl"
    executor = PaperExecutor(AppConfig(execution=ExecutionConfig(dry_run=False)), str(audit), True)
    try:
        executor.submit_market_order("TEST", 1, "buy", 10)
    except RuntimeError:
        assert '"ERROR"' in audit.read_text()
        return
    assert False
