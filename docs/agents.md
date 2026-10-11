# Agents autonomes simulés

Les agents du dépôt représentent des rôles inspirés d’une organisation de fonds fictive : Data Engineer, Quant Researcher, Risk Manager et Portfolio Manager. Ils peuvent observer les données, produire des propositions, se répondre par des objets structurés et sélectionner une proposition dans un cycle déterministe.

Le terme « autonomie » désigne ici une autonomie logicielle bornée : chaque agent exécute son contrat, garde une trace de son état et justifie sa sortie. Le système ne prétend pas créer une conscience réelle. Les limites de risque, le mode paper, le dry-run et l’absence d’ordres externes restent obligatoires et ne peuvent pas être contournés par un agent.

## Cycle actuel

```text
données CSV → Data Engineer → Quant Researcher → Risk Manager → Portfolio Manager → audit
```

`AutonomousSimulation` initialise une allocation de 1 000 000 000 AXE dans le registre Axe Coin, lance le cycle de travail et retourne un rapport structuré. Le cycle actuel ne simule pas encore de PnL ni d’enrichissement automatique du capital : l’offre initiale est une dotation fictive, et toute évolution du capital devra passer par un backtest explicite, des contrôles de risque et un audit.

## Règles d’autonomie

Les agents peuvent proposer ou refuser, mais jamais créer de valeur externe, modifier leurs propres limites, appeler une API live, envoyer un ordre sans les contrôles existants ou transférer Axe Coin hors du registre local. Une revue humaine reste disponible pour les décisions escaladées.
