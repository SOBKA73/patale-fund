from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

EVENTS = {"DECISION", "RISK_REFUSAL", "ORDER_INTENT", "ORDER_SENT", "DRY_RUN", "ERROR", "KILL_SWITCH"}


def append_event(path: str | Path, event_type: str, payload: dict, version: str = "unknown") -> None:
    if event_type not in EVENTS:
        raise ValueError("type d'événement inconnu")
    record = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "payload": payload,
        "code_version": version,
    }
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, sort_keys=True) + "\n")
