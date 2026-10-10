from decimal import Decimal

import pytest

from fond.config import TokenConfig
from fond.token import TokenError, TokenLedger


def ledger(events=None):
    return TokenLedger(
        TokenConfig(symbol="PAC-SIM", decimals=2, max_supply=Decimal("100.00"), issuer_account="treasury"),
        audit=(lambda event, payload: events.append((event, payload))) if events is not None else None,
    )


def test_issue_transfer_burn_and_audit():
    events = []
    book = ledger(events)
    book.issue("research", "50.00", "treasury")
    book.transfer("research", "portfolio", "12.50")
    book.burn("portfolio", "2.50")
    assert book.balance_of("research") == Decimal("37.50")
    assert book.balance_of("portfolio") == Decimal("10.00")
    assert book.outstanding == Decimal("47.50")
    assert [event for event, _ in events] == ["TOKEN_ISSUED", "TOKEN_TRANSFERRED", "TOKEN_BURNED"]


def test_issuer_and_supply_limits():
    book = ledger()
    with pytest.raises(TokenError):
        book.issue("research", "1.00", "not-treasury")
    book.issue("research", "100.00", "treasury")
    with pytest.raises(TokenError):
        book.issue("research", "0.01", "treasury")


def test_precision_and_balance_limits():
    book = ledger()
    with pytest.raises(TokenError):
        book.issue("research", "0.001", "treasury")
    with pytest.raises(TokenError):
        book.transfer("research", "portfolio", "1.00")
