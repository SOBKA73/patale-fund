# Architecture

Le flux du MVP est :

```text
CSV validé → signaux z-score → backtest / risk.py → exécution paper dry-run → audit JSONL
```

- `data.py` valide les prix et les dates.
- `strategy.py` produit des signaux long-only sans regard vers le futur.
- `backtest.py` applique sizing, frais et glissement de façon déterministe.
- `risk.py` expose des décisions structurées et un coupe-circuit journalier.
- `execution.py` refuse toute URL autre que l’endpoint paper Alpaca, et le dry-run est la valeur par défaut.
- `audit.py` écrit un événement par ligne dans `logs/`, exclu de Git.
