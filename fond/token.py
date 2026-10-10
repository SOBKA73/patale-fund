from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation
from typing import Callable

from .config import TokenConfig


class TokenError(ValueError):
    """Erreur métier du registre de jetons simulés."""


@dataclass
class TokenLedger:
    config: TokenConfig
    audit: Callable[[str, dict], None] | None = None
    balances: dict[str, Decimal] = field(default_factory=dict)
    issued: Decimal = Decimal("0")
    burned: Decimal = Decimal("0")

    def __post_init__(self) -> None:
        self.config.validate()

    @property
    def outstanding(self) -> Decimal:
        return self.issued - self.burned

    def _amount(self, value: str | int | float | Decimal) -> Decimal:
        try:
            amount = Decimal(str(value))
        except (InvalidOperation, ValueError) as exc:
            raise TokenError("montant de jetons invalide") from exc
        quantum = Decimal(1).scaleb(-self.config.decimals)
        if amount <= 0 or amount != amount.quantize(quantum):
            raise TokenError("montant positif avec une précision invalide")
        return amount

    def _account(self, account: str) -> str:
        value = account.strip()
        if not value or len(value) > 64 or any(c.isspace() for c in value):
            raise TokenError("compte invalide")
        return value

    def _emit(self, event: str, payload: dict) -> None:
        if self.audit:
            self.audit(event, payload)

    def issue(self, recipient: str, amount: str | int | float | Decimal, actor: str) -> Decimal:
        recipient = self._account(recipient)
        if actor != self.config.issuer_account:
            raise TokenError("seul le compte émetteur simulé peut créer des jetons")
        value = self._amount(amount)
        if self.outstanding + value > self.config.max_supply:
            raise TokenError("plafond d'émission dépassé")
        self.balances[recipient] = self.balances.get(recipient, Decimal("0")) + value
        self.issued += value
        self._emit("TOKEN_ISSUED", {"actor": actor, "recipient": recipient, "amount": str(value)})
        return value

    def transfer(self, sender: str, recipient: str, amount: str | int | float | Decimal) -> Decimal:
        sender, recipient = self._account(sender), self._account(recipient)
        value = self._amount(amount)
        if self.balances.get(sender, Decimal("0")) < value:
            raise TokenError("solde insuffisant")
        self.balances[sender] -= value
        self.balances[recipient] = self.balances.get(recipient, Decimal("0")) + value
        self._emit("TOKEN_TRANSFERRED", {"sender": sender, "recipient": recipient, "amount": str(value)})
        return value

    def burn(self, holder: str, amount: str | int | float | Decimal) -> Decimal:
        holder = self._account(holder)
        value = self._amount(amount)
        if self.balances.get(holder, Decimal("0")) < value:
            raise TokenError("solde insuffisant pour destruction")
        self.balances[holder] -= value
        self.burned += value
        self._emit("TOKEN_BURNED", {"holder": holder, "amount": str(value)})
        return value

    def balance_of(self, account: str) -> Decimal:
        return self.balances.get(self._account(account), Decimal("0"))

    def snapshot(self) -> dict[str, str | dict[str, str]]:
        return {
            "name": self.config.name,
            "symbol": self.config.symbol,
            "issued": str(self.issued),
            "burned": str(self.burned),
            "outstanding": str(self.outstanding),
            "balances": {key: str(value) for key, value in sorted(self.balances.items())},
        }
