SIMULATION INTERNE. Aucun capital réel. Document de travail, non destiné à un tiers ni à une offre de titres ou de services financiers.

# Organigramme — PATALE-EMPIRE-CAPITALE

**Statut : brouillon — à valider par le gestionnaire humain.**

## Objet et limites

Cet organigramme décrit dix postes de travail pour le simulateur interne de paper trading. Il ne constitue ni des statuts, ni un dossier d’agrément, ni un document destiné à un tiers. Les titulaires, seuils, fréquences et quorums ne sont pas arrêtés dans ce brouillon.

Le gestionnaire humain conserve la décision finale. Les mentions « agent » désignent une fonction opérée avec supervision humaine ; elles ne transfèrent pas la responsabilité finale.

## Schéma fonctionnel proposé

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
└── Conseil juridique externe
```

## Postes

### 1. Risk Manager — agent (supervision humaine)

- **Mission :** suivre les risques simulés, challenger les hypothèses et signaler les contrôles manquants, incidents et exceptions.
- **Reporting :** accès direct au gestionnaire humain ; échanges fonctionnels avec le Portfolio Manager, le Quant Researcher, le Middle et Back Office et la Cybersécurité.
- **Droit de veto éventuel :** peut proposer ou déclencher, selon l’option validée, une suspension préventive lorsqu’un contrôle critique manque ; toute action est consignée et revue par le gestionnaire humain.

### 2. Quant Researcher — agent (supervision humaine)

- **Mission :** formuler des hypothèses de recherche et documenter méthodes, limites statistiques et biais possibles.
- **Reporting :** Portfolio Manager pour les priorités de recherche ; Risk Manager pour les hypothèses et limites de risque.
- **Droit de veto éventuel :** aucun veto autonome proposé ; peut signaler un défaut méthodologique bloquant.

### 3. Data Engineer — agent (supervision humaine)

- **Mission :** organiser les données autorisées et documenter leur provenance, qualité, transformations et disponibilité.
- **Reporting :** Infrastructure et DevOps pour l’exploitation ; Quant Researcher et Risk Manager pour les exigences de qualité.
- **Droit de veto éventuel :** peut bloquer techniquement l’utilisation d’une donnée dont la provenance ou l’intégrité n’est pas documentée, sous revue humaine.

### 4. Quant Developer — agent (supervision humaine)

- **Mission :** développer les outils de recherche et de simulation autorisés dans les dépôts appropriés, avec tests et documentation.
- **Reporting :** Infrastructure et DevOps pour le cycle logiciel ; Quant Researcher pour les spécifications ; Risk Manager pour les contrôles requis.
- **Droit de veto éventuel :** aucun veto métier ; peut bloquer une mise en service simulée si les tests obligatoires échouent.

### 5. Portfolio Manager — humain ou agent, à valider

- **Mission :** coordonner les priorités du portefeuille simulé et présenter les propositions au gestionnaire humain.
- **Reporting :** gestionnaire humain ; coordination avec Risk Manager, RCCI et Middle et Back Office.
- **Droit de veto éventuel :** aucun veto définitif proposé ; peut demander le report d’une décision pour information incomplète.

### 6. RCCI — humain ou agent, à valider

- **Mission :** contrôler le respect des procédures internes simulées, les conflits de rôles et la traçabilité des décisions.
- **Reporting :** accès direct au gestionnaire humain ; indépendance fonctionnelle vis-à-vis du Portfolio Manager.
- **Droit de veto éventuel :** peut suspendre procéduralement une décision non documentée ou hors processus, jusqu’à correction et consignation.

### 7. Middle et Back Office — agent (supervision humaine)

- **Mission :** tenir les rapprochements et journaux opérationnels simulés et vérifier les états de paper trading.
- **Reporting :** gestionnaire humain pour la qualité opérationnelle ; coordination avec Risk Manager et Portfolio Manager.
- **Droit de veto éventuel :** peut bloquer une clôture ou un rapprochement simulé incomplet ou incohérent.

### 8. Infrastructure et DevOps — agent (supervision humaine)

- **Mission :** administrer les environnements autorisés, les sauvegardes, les contrôles d’accès techniques et la traçabilité des changements.
- **Reporting :** gestionnaire humain ; coordination avec Quant Developer, Data Engineer et Cybersécurité.
- **Droit de veto éventuel :** peut bloquer un déploiement présentant un risque technique critique ou sans retour arrière documenté.

### 9. Cybersécurité — agent (supervision humaine)

- **Mission :** définir les contrôles de sécurité, surveiller accès et dépendances, et contribuer aux revues d’incidents.
- **Reporting :** accès direct au gestionnaire humain ; coordination avec Infrastructure et DevOps et RCCI.
- **Droit de veto éventuel :** peut demander ou déclencher, selon l’option validée, la suspension d’un accès, déploiement ou intégration présentant un risque critique.

### 10. Conseil juridique externe — humain

- **Mission :** fournir ponctuellement un avis humain sur les questions soulevées par le gestionnaire humain et identifier les sujets nécessitant un conseil professionnel.
- **Reporting :** relation directe avec le gestionnaire humain, sur demande ; aucun reporting opérationnel vers un agent.
- **Droit de veto éventuel :** aucun veto opérationnel ; peut recommander de ne pas poursuivre une action et demander un avis avant toute suite.

## Points ouverts soumis au gestionnaire humain

Aucune option ci-dessous n’est adoptée dans ce brouillon. Pour chaque point, deux options au maximum sont proposées.

| Point | Option A | Option B | Conséquence à examiner |
|---|---|---|---|
| Titularité des postes | Postes opérationnels confiés à des humains | Postes opérationnels confiés à des agents avec supervision humaine | A clarifie la responsabilité ; B accélère l’exécution mais exige une supervision renforcée. |
| Veto critique | Suspension immédiate, revue humaine sous un délai à fixer | Recommandation de suspension, décision humaine préalable | A réduit le délai d’exposition ; B limite les interruptions mais peut retarder la protection. |
| Indépendance du RCCI | RCCI distinct du Portfolio Manager | Cumul temporaire en phase de démarrage | A renforce la séparation ; B simplifie le démarrage mais augmente le risque de conflit. |
| Traçabilité d’un veto | Journal avant toute levée | Journal dans le délai à fixer après levée | A renforce l’auditabilité ; B est plus souple mais laisse une période non documentée. |

**Le gestionnaire humain doit valider les choix avant toute activation ou rédaction de documents ultérieurs.**
