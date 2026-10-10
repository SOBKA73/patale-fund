# Procédure — cycle de vie d'une stratégie simulée

> **BROUILLON — à valider par le gestionnaire humain**
>
> **SIMULATION INTERNE. Aucun capital réel. Ce document ne constitue pas une offre de titres, de parts ou de services financiers et ne doit pas être diffusé à aucun tiers.**

## Périmètre

Cette procédure décrit le passage contrôlé d'une idée de recherche à une phase de paper trading. Elle ne crée ni stratégie, ni moteur de trading, ni module de risque dans ce dépôt.

## Étapes obligatoires

1. **Proposition.** Le Quant Researcher documente l'hypothèse, l'univers théorique, la logique, les données, les limites et le responsable. L'idée reçoit un identifiant dans `registres/registre_strategies.md` avec le statut « proposée ».
2. **Backtest.** Les résultats, paramètres, période, coûts simulés, biais possibles, données manquantes et code ou dépôt de référence sont documentés. Aucun résultat ne doit être présenté comme une garantie.
3. **Validation hors échantillon.** Une période ou un jeu de données non utilisé pour la conception est défini avant l'examen. Le Risk Manager examine les biais, la robustesse et les limites ; un résultat insuffisant entraîne un retour en recherche ou un abandon.
4. **Décision documentée.** Le comité d'investissement simulé examine le dossier. La décision, sa justification, les abstentions et les vetos sont consignés. Les options ouvertes de gouvernance ne sont pas réputées approuvées par défaut.
5. **Paper trading.** La stratégie autorisée est exécutée uniquement dans l'environnement simulé approuvé, avec suivi des données, versions, incidents et écarts entre hypothèses et observations.
6. **Revue.** Une revue périodique examine les résultats simulés, les écarts, les incidents, les changements et la poursuite, la suspension ou la clôture. Le statut du registre est mis à jour.

## Sorties minimales

Chaque étape produit une trace datée, un auteur, une décision ou un statut, une justification, les références utiles et les actions de suivi. Le passage à l'étape suivante nécessite que les contrôles obligatoires soient présents ou qu'une exception soit explicitement approuvée et journalisée.
