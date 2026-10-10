import json

from fond.audit import append_event


def test_one_json_line_per_event(tmp_path):
    p = tmp_path / "logs" / "audit.jsonl"
    append_event(p, "DRY_RUN", {"qty": 1})
    append_event(p, "ERROR", {"message": "x"})
    assert len(p.read_text().splitlines()) == 2
    assert json.loads(p.read_text().splitlines()[0])["event_type"] == "DRY_RUN"
