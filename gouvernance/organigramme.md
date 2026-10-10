# Organigramme — PATALE-EMPIRE-CAPITALE

> **BROUILLON — à valider par le gestionnaire humain**
>
> **SIMULATION INTERNE. Aucun capital réel. Ce document ne constitue pas une offre de titres, de parts ou de services financiers et ne doit pas être diffusé à aucun tiers.**

## 1. Objet et limites

Cet organigramme décrit les rôles de travail du simulateur interne de paper trading. Il ne constitue pas des statuts, un document d'immatriculation, un dossier d'agrément ou un document destiné à des investisseurs.

Les noms des titulaires et les seuils de veto ne sont pas arrêtés dans ce brouillon. Ils doivent être validés par le gestionnaire humain avant activation.

## 2. Schéma fonctionnel

```text
Gestionnaire humain / responsable de la simulation
├── Portfolio Manager
├── Risk Manager
├── RCCI
├── Quant Researcher
├── Quant Developer
├── Data Engineer
├── Middle et Back Office
├── Infrastructure et DevOps
├── Cybersécurité
└── Conseil juridique externe (humain, consulté ponctuellement)
```

Le **Conseil juridique externe** est un intervenant humain ponctuel. Il ne reçoit pas de mandat d'exécution technique et ne remplace pas une validation du gestionnaire humain.

## 3. Postes et responsabilités

### 3.1 Risk Manager

- **Responsabilités :** définir et maintenir le cadre de suivi des risques simulés ; challenger les hypothèses ; examiner les dépassements, incidents et exceptions ; recommander une suspension lorsque les contrôles sont insuffisants.
- **Titulaire :** agent ou personne à désigner ; titulaire intérimaire proposé : gestionnaire humain jusqu'à validation.
- **Reporting :** accès direct au gestionnaire humain ; échanges fonctionnels avec le Portfolio Manager, le Quant Researcher, le Middle et Back Office et la Cybersécurité.
- **Veto éventuel :** suspension préventive d'une stratégie ou d'une expérimentation en cas de contrôle critique manquant, sous réserve de consignation et de revue humaine.

### 3.2 Quant Researcher

- **Responsabilités :** formuler des hypothèses de recherche ; documenter les méthodes de recherche et de backtest ; signaler les limites statistiques et les biais possibles.
- **Titulaire :** agent de recherche quantitatif à désigner.
- **Reporting :** Portfolio Manager pour les priorités de recherche ; Risk Manager pour les hypothèses et limites de risque.
- **Veto éventuel :** aucun veto autonome proposé ; obligation de signaler tout défaut méthodologique bloquant.

### 3.3 Data Engineer

- **Responsabilités :** organiser les jeux de données autorisés ; documenter la provenance, la qualité, les transformations et la disponibilité des données de simulation.
- **Titulaire :** agent data à désigner.
- **Reporting :** Infrastructure et DevOps pour l'exploitation ; Risk Manager et Quant Researcher pour les exigences de qualité.
- **Veto éventuel :** blocage technique de l'utilisation d'un jeu de données dont la provenance ou l'intégrité n'est pas documentée.

### 3.4 Quant Developer

- **Responsabilités :** implémenter les outils de recherche et de simulation autorisés dans les dépôts appropriés ; fournir des tests et une documentation technique ; respecter la revue des changements.
- **Titulaire :** agent de développement quantitatif à désigner.
- **Reporting :** Infrastructure et DevOps pour le cycle logiciel ; Quant Researcher pour les spécifications ; Risk Manager pour les contrôles requis.
- **Veto éventuel :** aucun veto métier autonome ; peut bloquer une mise en production simulée si les tests obligatoires échouent.

### 3.5 Portfolio Manager

- **Responsabilités :** coordonner les priorités de portefeuille simulé ; proposer l'examen de stratégies ; présenter les décisions au comité compétent ; veiller à la cohérence avec le mandat pédagogique.
- **Titulaire :** personne ou agent à désigner ; ne peut pas s'auto-attribuer une validation finale non prévue par la gouvernance.
- **Reporting :** gestionnaire humain ; coordination avec Risk Manager, RCCI et Middle et Back Office.
- **Veto éventuel :** aucun veto définitif proposé ; peut demander le report d'une décision pour information incomplète.

### 3.6 RCCI

- **Responsabilités :** contrôler le respect des procédures internes simulées ; suivre les conflits de rôles ; vérifier la traçabilité des décisions et des exceptions.
- **Titulaire :** personne ou agent de contrôle à désigner, indépendant du Portfolio Manager.
- **Reporting :** accès direct au gestionnaire humain ; ne reçoit pas d'instruction opérationnelle du Portfolio Manager pour ses contrôles.
- **Veto éventuel :** suspension procédurale d'une décision non documentée ou prise hors du processus approuvé, jusqu'à correction et consignation.

### 3.7 Middle et Back Office

- **Responsabilités :** tenir les rapprochements et journaux opérationnels simulés ; vérifier les états de paper trading ; suivre les événements, validations et pièces justificatives internes.
- **Titulaire :** agent ou personne à désigner.
- **Reporting :** gestionnaire humain pour la qualité opérationnelle ; coordination avec Risk Manager et Portfolio Manager.
- **Veto éventuel :** blocage d'une clôture ou d'un rapprochement simulé incomplet ou incohérent.

### 3.8 Infrastructure et DevOps

- **Responsabilités :** administrer les environnements de travail autorisés ; gérer les déploiements, sauvegardes et contrôles d'accès techniques ; maintenir la traçabilité des changements.
- **Titulaire :** agent infrastructure à désigner.
- **Reporting :** gestionnaire humain ; coordination avec Quant Developer, Data Engineer et Cybersécurité.
- **Veto éventuel :** blocage d'un déploiement présentant un risque technique critique ou une absence de retour arrière documenté.

### 3.9 Cybersécurité

- **Responsabilités :** définir les contrôles de sécurité ; surveiller les secrets, accès, dépendances et incidents ; recommander la mise en quarantaine d'un composant compromis ; contribuer aux revues d'incidents.
- **Titulaire :** agent ou personne cybersécurité à désigner, indépendant des développeurs lorsque cela est possible.
- **Reporting :** accès direct au gestionnaire humain ; coordination avec Infrastructure et DevOps et RCCI.
- **Veto éventuel :** suspension immédiate d'un accès, d'un déploiement ou d'une intégration présentant un risque de sécurité critique, avec journalisation et revue humaine rapide.

### 3.10 Conseil juridique externe

- **Responsabilités :** fournir un avis humain ponctuel sur les questions juridiques soulevées par le gestionnaire humain ; identifier les sujets nécessitant un conseil professionnel.
- **Titulaire :** humain externe à consulter ponctuellement ; aucun agent IA ne tient ce rôle.
- **Reporting :** relation directe avec le gestionnaire humain, sur demande ; pas de reporting opérationnel vers un agent.
- **Veto éventuel :** aucun veto opérationnel ; peut recommander de ne pas poursuivre une action et demander une validation juridique avant toute suite.

## 4. Séparation minimale des responsabilités

- Le Portfolio Manager ne valide pas seul ses propres contrôles de risque ou de conformité.
- Le Risk Manager, le RCCI et la Cybersécurité doivent pouvoir signaler directement un blocage au gestionnaire humain.
- Les changements techniques sont soumis à une revue indépendante de leur auteur lorsque les ressources le permettent.
- Les décisions, vetos, levées de veto et exceptions sont consignés dans les registres prévus à cet effet.

## 5. Points ouverts à trancher par le gestionnaire humain

Les choix suivants ne sont pas décidés dans ce brouillon. Deux options sont proposées pour chacun afin d'éviter toute décision implicite.

| Point | Option A | Option B | Conséquence à examiner |
|---|---|---|---|
| Titularité des rôles | Titulaires humains nommés par rôle | Agents IA désignés avec supervision humaine | L'option A clarifie la responsabilité ; l'option B accélère l'exécution mais exige des contrôles et une supervision renforcés. |
| Veto de sécurité | Veto immédiat, revue humaine sous 24 h | Recommandation de suspension, décision humaine avant blocage | L'option A réduit l'exposition à un incident ; l'option B limite les interruptions mais augmente le risque de délai. |
| Indépendance du RCCI | RCCI distinct du Portfolio Manager | RCCI cumulable temporairement en phase de démarrage | L'option A renforce la séparation ; l'option B simplifie le démarrage mais crée un risque de conflit de rôles. |
| Traçabilité | Journal obligatoire avant toute levée de veto | Journal sous 1 jour ouvré après levée de veto | L'option A renforce l'auditabilité ; l'option B est plus souple mais peut laisser une période non documentée. |

**Aucune option ci-dessus n'est adoptée tant que le gestionnaire humain n'a pas validé le choix.**
