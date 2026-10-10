# Procédure — revue des changements de code et de documentation

> **BROUILLON — à valider par le gestionnaire humain**
>
> **SIMULATION INTERNE. Aucun capital réel. Ce document ne constitue pas une offre de titres, de parts ou de services financiers et ne doit pas être diffusé à aucun tiers.**

## Périmètre

La procédure s'applique aux changements de documentation de ce dépôt et renvoie aux dépôts techniques pour les changements de code. Aucun code de trading, module de risque ou stratégie ne doit être ajouté ici.

## Étapes

1. Créer une branche dédiée et décrire l'objectif, le périmètre et les points ouverts.
2. Produire une pull request vers `main`; aucun changement direct sur `main`.
3. Vérifier le cadre obligatoire, le marquage brouillon, la cohérence avec les registres et l'absence de secrets ou données personnelles.
4. Obtenir une revue par une personne distincte de l'auteur lorsque possible. Pour un sujet de risque, conformité ou sécurité, demander la revue du rôle compétent.
5. Documenter les commentaires, corrections, abstentions et éventuels vetos dans la pull request ou les registres appropriés.
6. Fusionner seulement après validation requise et conserver le lien de la pull request comme trace.

## Retour arrière et clôture

Un changement problématique est suspendu ou annulé par une nouvelle pull request documentée. La clôture vérifie les liens, les versions et les actions de suivi. Toute exception de revue est justifiée et validée humainement.

## Choix à valider

Option A : une approbation indépendante pour tout changement. Option B : revue renforcée seulement pour les changements à risque et auto-vérification documentée pour les changements éditoriaux mineurs. L'option A maximise la traçabilité ; l'option B accélère les corrections simples.
