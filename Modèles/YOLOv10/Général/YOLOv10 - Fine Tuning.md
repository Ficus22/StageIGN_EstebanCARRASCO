---
tags:
  - recherches
Date: 2025-05-21
References: "[[Bibliographie.canvas|Bibliographie]]"
Objectif: Chercher comment améliorer la spécificité du modèle
aliases:
---
# Les étapes du Fine-Tuning
## 1- Préparation du dataset
Il s'agit d'organiser son dataset en un set d'entraînement et un set de validation. Il faut s'assurer que chaque image est labellisée avec des bounding box, and que les classes correspondent à celles définit dans le fichier de configuration.

## 2- Ajustement et configuration
Ensuite, il faut modifier le fichier de [[YOLOv10 - Configuration du modèle|configuration du modèle]] pour qu'il corresponde à notre dataset et nos attentes. C'est-à-dire, qu'il faut confirmer la nature et le nombre de classes, les [[YOLOv10 - Anchor boxes|anchor boxes]] et les chemins des dossiers des différents sets de données. 

## 3- Utilisation de poids pré-entraînés
## 4- Entraînement
## 5- Évaluation
## 6- Itérations
## 7- Inférence
