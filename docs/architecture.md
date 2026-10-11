# Architecture

Le flux du MVP est :

```text
CSV validé → signaux z-score → backtest / risk.py → exécution paper dry-run → audit JSONL
```

Le comité d’agents simulés ajoute un cycle local, rejouable et borné :

```text
Data Engineer → Quant Researcher ⇄ débat Quant–Risk → Portfolio Manager → rapport audité
```

- `data.py` valide les prix et les dates.
- `strategy.py` produit des signaux long-only sans regard vers le futur.
- `backtest.py` applique sizing, frais et glissement de façon déterministe.
- `risk.py` expose des décisions structurées et un coupe-circuit journalier.
- `execution.py` refuse toute URL autre que l’endpoint paper Alpaca, et le dry-run est la valeur par défaut.
- `audit.py` écrit un événement par ligne dans `logs/`, exclu de Git.
- `fond/agents/` contient les contrats, messages, registre et orchestrateur des agents.
- `fond/agents/debate.py` impose l’approbation explicite de Risk, son veto bloquant et l’escalade des désaccords.
- L’orchestrateur bootstrappe 1 000 000 000 AXE dans le registre local ; il ne crée pas de valeur externe et ne produit aucun ordre réseau.
