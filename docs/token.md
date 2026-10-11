# Axe Coin — jeton interne simulé

**Axe Coin (`AXE`)** est un jeton numérique fictif réservé au registre interne du laboratoire. Il n’est ni une monnaie ayant cours légal, ni un actif financier, ni une créance, ni une unité convertible. Il ne peut pas être transféré hors du dépôt et n’est relié à aucune blockchain, aucun portefeuille externe, aucun compte bancaire ou aucun service distant.

## Règles du MVP

Le registre `fond/token.py` utilise `Decimal` pour éviter les erreurs d’arrondi. L’offre maximale configurée est de **1 000 000 000 AXE**, avec six décimales. Seul le compte émetteur simulé peut créer des jetons ; les transferts exigent un solde suffisant ; la destruction réduit l’offre en circulation. Chaque opération peut produire un événement d’audit append-only.

Le jeton ne doit pas être utilisé pour conclure une vente, solliciter des fonds, promettre une valeur, rémunérer un tiers ou représenter une participation dans le fonds. Toute extension vers une blockchain, une convertibilité, un marché secondaire, des comptes de tiers ou une valeur externe est hors périmètre et nécessite une décision séparée ainsi qu’un avis juridique externe.

## Exemple local

```python
from fond.config import load_config
from fond.token import TokenLedger

ledger = TokenLedger(load_config().token)
ledger.issue("portfolio", "100.000000", "treasury")
ledger.transfer("portfolio", "strategy-lab", "5.000000")
print(ledger.snapshot())
```
