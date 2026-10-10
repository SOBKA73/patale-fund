from __future__ import annotations

from .audit import append_event
from .config import PAPER_URL, AppConfig, paper_credentials


class PaperExecutor:
    def __init__(self, config: AppConfig, audit_path: str = "logs/audit.jsonl", send_paper_orders: bool = False):
        config.validate()
        if config.execution.base_url != PAPER_URL:
            raise ValueError("URL non paper refusée")
        self.config, self.audit_path, self.send = config, audit_path, send_paper_orders
        self.client = None
        if send_paper_orders and not config.execution.dry_run:
            key, secret = paper_credentials()
            from alpaca.trading.client import TradingClient

            self.client = TradingClient(key, secret, paper=True, url_override=PAPER_URL)

    def submit_market_order(self, symbol: str, qty: int, side: str, price: float) -> dict:
        if self.config.execution.base_url != PAPER_URL:
            raise ValueError("URL non paper refusée")
        if side not in {"buy", "sell"} or qty <= 0:
            raise ValueError("ordre invalide")
        intent = {"symbol": symbol, "qty": qty, "side": side, "type": "market", "price": price}
        if not self.send or self.config.execution.dry_run:
            append_event(self.audit_path, "DRY_RUN", intent)
            return {"status": "DRY_RUN", **intent}
        append_event(self.audit_path, "ORDER_INTENT", intent)
        try:
            from alpaca.trading.enums import OrderSide, TimeInForce
            from alpaca.trading.requests import MarketOrderRequest

            order = self.client.submit_order(
                MarketOrderRequest(
                    symbol=symbol,
                    qty=qty,
                    side=OrderSide.BUY if side == "buy" else OrderSide.SELL,
                    time_in_force=TimeInForce.DAY,
                )
            )
            append_event(self.audit_path, "ORDER_SENT", {"id": str(order.id), **intent})
            return {"status": "ORDER_SENT", "id": str(order.id), **intent}
        except Exception as exc:
            append_event(self.audit_path, "ERROR", {"error": type(exc).__name__, "message": str(exc)})
            raise
