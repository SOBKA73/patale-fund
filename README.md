# PATALE-EMPIRE-CAPITALE — documentation interne

> **BROUILLON — à valider par le gestionnaire humain**
>
> **SIMULATION INTERNE. Aucun capital réel. Ce document ne constitue pas une offre de titres, de parts ou de services financiers et ne doit pas être diffusé à aucun tiers.**

## Objet du dépôt

Ce dépôt rassemble la documentation interne du fonds **SIMULÉ PATALE-EMPIRE-CAPITALE** pour un environnement pédagogique et de recherche consacré au **paper trading**. Il décrit l'organisation, les responsabilités, les procédures de contrôle et les registres de décision du simulateur.

Le dépôt ne contient ni moteur de trading, ni module de risque, ni stratégie de trading. Ces composants relèvent d'autres dépôts et d'étapes distinctes.

## Périmètre

Le contenu est limité à des outils de travail internes pour la simulation :

- gouvernance et organigramme ;
- fiches de mandat des agents et rôles humains ;
- procédures internes ;
- journaux et registres ;
- glossaire commun.

Les documents restent marqués **brouillon** tant qu'ils n'ont pas été validés par le gestionnaire humain.

## Dépôts associés

- `patale-fund` — gouvernance, procédures, mandats et registres de la simulation ;
- `patale-risk` — dépôt prévu pour les travaux de risque, hors périmètre de ce dépôt ;
- autres dépôts — à ajouter après validation humaine de leur périmètre.

## Règles de sécurité et d'usage

- Aucun capital réel n'est utilisé.
- Aucune clé, aucun identifiant de broker réel et aucune donnée personnelle de tiers ne doivent être ajoutés.
- Aucun contenu destiné à des investisseurs, prospectus, note d'information, pitch, contenu marketing ou promesse de rendement ne doit être produit ici.
- Les besoins éventuels en statuts, immatriculation ou agrément sont uniquement consignés comme questions à soumettre à un avocat ; ils ne sont pas rédigés dans ce dépôt.
- Les documents sont internes et ne doivent pas être diffusés à des tiers.

## Workflow de contribution

1. Créer une branche dédiée à chaque livrable ou lot cohérent.
2. Ne jamais pousser directement sur `main`.
3. Décrire clairement le périmètre, les hypothèses et les points ouverts dans la pull request.
4. Ouvrir une pull request pour chaque lot.
5. Marquer tout document non validé comme **brouillon**.
6. Lorsqu'une décision de gouvernance n'est pas tranchée, proposer deux options avec leurs conséquences et laisser le choix au gestionnaire humain.
7. Obtenir une validation humaine avant de produire les mandats détaillés des agents.

## État du premier lot

Ce premier lot contient :

- `README.md` ;
- `gouvernance/organigramme.md`.

La charte des comités, les mandats, les procédures et les registres seront traités dans des lots ultérieurs après validation humaine de ce premier lot.

## Licence et diffusion

Aucune licence de diffusion externe n'est définie à ce stade. Toute réutilisation ou diffusion doit faire l'objet d'une validation humaine préalable.
