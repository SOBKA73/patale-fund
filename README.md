# PATALE-EMPIRE-CAPITALE — Axe Capital MVP

> **SIMULATION UNIQUEMENT.** Aucun capital réel, aucun compte réel, aucune promesse de rendement et aucun conseil en investissement. Projet de recherche open source en paper trading.

Ce dépôt contient un squelette testé d’un moteur de données, stratégie placeholder, backtest, garde-fous, exécution paper et audit. La stratégie de retour à la moyenne par z-score valide l’architecture uniquement ; aucune conclusion de rentabilité n’est produite.

## Installation

Python 3.11 est requis. Installation locale recommandée :

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e '.[dev]'
```

Les clés `ALPACA_API_KEY` et `ALPACA_SECRET_KEY` ne sont jamais versionnées. Elles ne sont nécessaires que pour un envoi paper explicitement demandé ; `.env.example` ne contient que les noms de variables.

## Commandes

```bash
python scripts/generate_sample_data.py
pytest
ruff check .
ruff format --check .
python -m fond backtest --data data/sample/prices.csv --config config.toml
```

Le mode `paper` est dry-run par défaut. L’envoi paper exige à la fois `--send-paper-orders`, `dry_run = false`, les deux variables d’environnement et l’URL exacte `https://paper-api.alpaca.markets`. Aucun appel live n’est accepté.

Le registre `Axe Coin (AXE)` est une monnaie interne fictive sans valeur réelle, sans blockchain et sans transfert externe. L’allocation initiale simulée est de 1 000 000 000 AXE. Ses règles sont documentées dans [`docs/token.md`](docs/token.md). Les agents autonomes simulés sont décrits dans [`docs/agents.md`](docs/agents.md).

## Structure

`fond/` contient les modules du moteur, du registre Axe Coin et des agents simulés ; `tests/` contient les tests sans réseau ; `data/sample/` contient des données synthétiques reproductibles ; `docs/` contient l’architecture, les décisions, les licences, le registre de jetons et la thèse à compléter par le propriétaire. `logs/` et les données brutes sont ignorés par Git.

## Contributions

Toute modification passe par une branche et une pull request. Aucun secret, donnée sensible ou clé ne doit apparaître dans le code, la configuration, les tests, les issues, la documentation ou l’historique.
