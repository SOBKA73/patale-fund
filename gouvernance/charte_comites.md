# Charte des comités internes simulés

> **BROUILLON — à valider par le gestionnaire humain**
>
> **SIMULATION INTERNE. Aucun capital réel. Ce document ne constitue pas une offre de titres, de parts ou de services financiers et ne doit pas être diffusé à aucun tiers.**

## 1. Objet et périmètre

Cette charte décrit le fonctionnement des comités du simulateur interne de paper trading. Elle ne constitue ni des statuts, ni un document d'immatriculation, ni un dossier d'agrément. Aucun comité ne gère de capital réel et aucune décision ne constitue une offre ou une recommandation destinée à des tiers.

Les seuils, fréquences et quorums ci-dessous sont des propositions de travail. Ils ne deviennent applicables qu'après validation humaine et consignation de cette validation dans `registres/journal_decisions.md`.

## 2. Principes communs

Chaque comité doit disposer d'un ordre du jour, des documents examinés, d'une liste des participants, des conflits ou abstentions éventuels, d'une décision et d'une justification. Les avis divergents, vetos et actions de suivi sont consignés. Une décision ne peut pas être réputée approuvée par silence.

Le Portfolio Manager ne peut pas valider seul une décision qui concerne ses propres contrôles. Le Risk Manager, le RCCI et la Cybersécurité peuvent porter un blocage au gestionnaire humain. Le Conseil juridique externe est un humain consulté ponctuellement et n'est pas membre permanent d'un comité.

## 3. Comité des risques

**Mission.** Examiner les risques méthodologiques, opérationnels, de données, de modèle, de sécurité et de processus liés aux travaux de simulation.

**Fréquence proposée.** Réunion mensuelle et réunion exceptionnelle en cas d'incident critique, de changement important ou de demande de veto.

**Participants.** Risk Manager, RCCI, Portfolio Manager, Data Engineer ou Quant Researcher selon le sujet, Cybersécurité lorsque la sécurité est concernée, et gestionnaire humain ou délégué.

**Quorum proposé.** Option A : trois participants, dont le Risk Manager ou le RCCI. Option B : majorité des participants désignés, dont obligatoirement le Risk Manager et le RCCI. L'option A facilite la tenue des réunions ; l'option B renforce la représentation mais peut retarder les décisions.

**Décision.** Le comité formule une décision ou une recommandation documentée. Un veto de sécurité ou de contrôle critique suspend l'action concernée jusqu'à levée explicite. Le gestionnaire humain tranche les désaccords non résolus.

## 4. Comité d'investissement simulé

**Mission.** Examiner les propositions de stratégies et les décisions de passage entre recherche, validation hors échantillon et paper trading. Il ne décide d'aucun investissement réel.

**Fréquence proposée.** Réunion à la demande pour une proposition complète, avec revue mensuelle des stratégies déjà en paper trading.

**Participants.** Portfolio Manager, Quant Researcher, Risk Manager, RCCI et gestionnaire humain ou délégué. Le Quant Developer et le Data Engineer participent lorsque leurs travaux sont directement examinés.

**Quorum proposé.** Option A : quatre participants, dont Portfolio Manager, Risk Manager et RCCI. Option B : tous les rôles permanents, sauf absence excusée et documentée. L'option A est plus opérationnelle ; l'option B réduit le risque de décision avec information manquante mais augmente le coût de coordination.

**Décision.** Le comité peut approuver une étape de simulation, demander des compléments, ajourner ou refuser. La justification doit distinguer les faits observés, les hypothèses et les limites. Aucune décision ne peut être formulée comme une promesse de rendement.

## 5. Revue mensuelle

**Mission.** Examiner l'état des stratégies, les incidents, les vetos, les changements de code, la qualité des données, les décisions en attente et le respect du périmètre documentaire.

**Fréquence.** Une fois par mois, à une date définie par le gestionnaire humain. Une revue supplémentaire peut être déclenchée après un incident critique.

**Participants.** Gestionnaire humain, Risk Manager, RCCI, Portfolio Manager, Middle et Back Office, Infrastructure et DevOps, et représentants techniques ou cybersécurité selon les sujets.

**Quorum proposé.** Option A : gestionnaire humain ou délégué, Risk Manager et RCCI. Option B : majorité des rôles permanents avec présence du gestionnaire humain ou de son délégué. L'option A garantit un contrôle minimal ; l'option B donne une vue plus complète mais peut retarder la revue.

**Sortie attendue.** Un compte rendu indiquant les indicateurs examinés, les décisions, les actions, les responsables, les échéances et les points à soumettre à validation humaine.

## 6. Processus de décision et consignation

Avant chaque séance, le secrétaire de séance prépare l'ordre du jour et les références internes. Pendant la séance, les participants déclarent leurs conflits ou abstentions. Après la séance, le compte rendu est soumis aux participants pour correction factuelle, puis enregistré dans le registre approprié.

Chaque entrée de registre comporte au minimum une date, un auteur, l'instance, le sujet, la décision ou le veto, sa justification, les participants essentiels et les actions de suivi. Une décision non tranchée est enregistrée comme « en attente » et ne doit pas être présentée comme approuvée.

Les changements au présent document suivent la revue des changements de code documentaire et font l'objet d'une pull request distincte.

## 7. Choix restant à valider

Le gestionnaire humain doit choisir une option pour chaque quorum proposé et fixer les fréquences définitives. Tant que ce choix n'est pas consigné, les options restent ouvertes et aucune règle chiffrée ne doit être appliquée par défaut.
