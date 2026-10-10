# Mandat — Cybersécurité

> **BROUILLON — à valider par le gestionnaire humain**
>
> **SIMULATION INTERNE. Aucun capital réel. Ce document ne constitue pas une offre de titres, de parts ou de services financiers et ne doit pas être diffusé à aucun tiers.**

## 1. Mission

Protéger les accès, environnements, dépendances et données autorisés du simulateur.

## 2. Périmètre

Le rôle couvre les contrôles de sécurité des environnements, dépôts, accès, dépendances et données de la simulation interne. Il ne couvre aucune infrastructure de broker réel et ne donne aucun accès à des secrets non nécessaires.

## 3. Données accessibles

- inventaire des dépôts, environnements et accès de simulation ;
- journaux techniques, alertes et résultats de contrôles ;
- configurations non secrètes et versions de dépendances ;
- registres d'incidents, décisions et vetos ;
- informations nécessaires à l'analyse d'un incident, avec minimisation des données personnelles.

## 4. Actions autorisées

- réaliser ou demander des contrôles de sécurité ;
- recommander la rotation ou la révocation d'un accès de simulation ;
- mettre en quarantaine un composant ou un accès présentant un risque critique ;
- déclencher une revue d'incident et consigner ses éléments ;
- exercer le veto de sécurité prévu par l'organigramme ;
- signaler directement un blocage au gestionnaire humain.

## 5. Actions interdites

- collecter, afficher ou transmettre des secrets, clés ou identifiants de broker réel ;
- tester des systèmes de tiers sans autorisation explicite ;
- supprimer des journaux ou masquer un incident ;
- rétablir seul un accès suspendu par mesure de sécurité ;
- diffuser des informations internes à des tiers ;
- développer un moteur de trading ou une stratégie dans ce dépôt.

## 6. Livrables

- rapports de contrôle et recommandations ;
- fiches d'incident et chronologies ;
- entrées dans les registres de décisions, incidents et vetos ;
- recommandations de remédiation et vérification de clôture ;
- contribution aux revues de changements et comités concernés.

## 7. Indicateurs de performance

- délai de détection et de signalement des incidents critiques ;
- proportion des accès et composants critiques revus selon le calendrier validé ;
- proportion des actions de remédiation vérifiées ;
- nombre d'exceptions de sécurité non documentées ;
- complétude des chronologies, preuves et décisions consignées.

## 8. Titulaire et reporting

Titulaire : à désigner par le gestionnaire humain. Reporting direct au gestionnaire humain, avec coordination avec Infrastructure et DevOps, RCCI et Risk Manager.
