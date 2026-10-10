from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .models import AgentIdentity


@dataclass(frozen=True)
class AgentMessage:
    sender: AgentIdentity
    recipient: AgentIdentity
    message_type: str
    payload: dict[str, Any]

    def as_dict(self) -> dict[str, Any]:
        return {
            "sender": self.sender.name,
            "recipient": self.recipient.name,
            "message_type": self.message_type,
            "payload": self.payload,
        }
