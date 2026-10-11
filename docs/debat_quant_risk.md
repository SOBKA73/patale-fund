# Protocole de communication et de débat Quant–Risk

**Statut : proposition opérationnelle à valider par le gestionnaire humain.** Ce protocole s’applique avant toute sélection d’ordre, même en paper trading. Les agents restent simulés : ils n’ont pas de conscience réelle et ne peuvent pas sortir du périmètre du dépôt.

## Rôles

- **Quant Researcher** : formule une proposition structurée, cite les données utilisées, expose l’hypothèse, le signal, la taille et les risques connus. Il ne peut pas s’auto-approuver.
- **Risk Manager** : vérifie indépendamment la taille, le levier, les pertes et les contraintes de risque. Il détient un **droit de veto bloquant** et ne peut pas être remplacé par le Quant.
- **Portfolio Manager** : ne sélectionne qu’une proposition explicitement approuvée par Risk. Il ne peut pas transformer un veto en approbation.

## Format obligatoire d’un message

Chaque message est structuré et auditable :

```text
agent, rôle, numéro de tour, type de message,
actif, action, taille, confiance,
justification, données utilisées, risques connus, contraintes
```

Les affirmations doivent être reproductibles à partir des données locales. Les messages vagues, non sourcés ou fondés sur une donnée future sont rejetés.

## Séquence standard

1. **Proposition Quant** : signal, action, taille, confiance, justification et preuves.
2. **Objection ou approbation Risk** : contrôle indépendant de la position et du levier ; chaque refus doit citer la règle déclenchée.
3. **Réponse Quant, au maximum une fois** : le Quant peut apporter une preuve déjà disponible ou réduire la taille. Il ne peut pas modifier les limites de Risk, inventer une donnée ou demander une exception implicite.
4. **Décision finale Risk** : approbation explicite, veto explicite ou escalade.
5. **Sélection Portfolio** : possible uniquement après approbation Risk.
6. **Exécution** : soumise aux contrôles existants, au dry-run et au mode paper-only.

La politique par défaut est de **deux tours maximum** : proposition/objection, puis réponse/décision. Une proposition approuvée directement doit tout de même contenir un événement `RISK_APPROVAL`.

## Désaccords et veto

- Un veto Risk est bloquant, même si le Quant a une confiance élevée.
- Un désaccord persistant après la réponse Quant reste `VETOED` ; aucun ordre n’est créé.
- Une donnée manquante, contradictoire ou non reproductible entraîne un refus ou une escalade.
- Le Portfolio Manager ne peut pas approuver seul une proposition refusée.
- Toute modification des limites de risque est hors débat et doit faire l’objet d’une décision séparée.

## Deux options de gouvernance

- **Option A — recommandée : deux tours et veto immédiat final.** Faible latence, traçabilité simple, protection forte ; peut écarter une idée qui nécessiterait davantage d’analyse.
- **Option B — à valider : trois tours maximum.** Permet une seconde réponse argumentée ; augmente la latence et le risque de débats répétitifs sans améliorer nécessairement la décision.

Le code utilise l’Option A par défaut. Le choix final de la fréquence, du quorum éventuel et des exceptions doit être validé par le gestionnaire humain.
