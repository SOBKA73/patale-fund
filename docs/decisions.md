# Décisions techniques

| Date | Choix | Alternative écartée | Raison |
|---|---|---|---|
| 2026-10-10 | CSV comme source primaire | API distante par défaut | Tests déterministes et sans réseau. |
| 2026-10-10 | `pandas` pour les séries et validations | Implémentation tabulaire maison | Lisibilité et validation de données. |
| 2026-10-10 | MIT proposée | Apache-2.0 | Licence permissive courte ; validation propriétaire requise. |
| 2026-10-10 | Dry-run par défaut | Envoi paper implicite | Évite tout ordre sans flag explicite. |
| 2026-10-10 | `PAC-SIM` comme jeton interne simulé | Blockchain ou token externe | Registre local déterministe, sans valeur réelle ni dépendance réseau. |
