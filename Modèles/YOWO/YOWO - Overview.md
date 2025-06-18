---
tags:
  - overview
Date: 2025-06-18
References: "[[Bibliographie.canvas|Bibliographie]]"
Objectif: Explications
aliases:
---
## Fonctionnement de YOWO

YOWO (You Only Watch Once) est une architecture de réseau de neurones convolutifs (CNN) unifiée pour la localisation spatio-temporelle des actions en temps réel dans les flux vidéo. Contrairement aux approches traditionnelles qui séparent la détection humaine et la classification d’action, YOWO traite ces deux tâches simultanément dans un cadre end-to-end. L’entrée du modèle est un clip vidéo composé de plusieurs images successives, et la sortie consiste en la prédiction des positions des bounding boxes ainsi que des labels d’action pour l’image courante. Les détections peuvent ensuite être reliées pour générer des « action tubes » sur toute la séquence vidéo.

L’architecture de YOWO repose sur deux branches principales :

- Une branche 2D CNN pour l’extraction des informations spatiales à partir de la frame clé.
- Une branche 3D CNN pour l’extraction des informations temporelles sur la séquence de frames.

Les deux branches sont fusionnées pour produire des prédictions de localisation et de classification en une seule passe, ce qui garantit des performances en temps réel (jusqu’à 34 FPS sur des clips de 16 frames).

## Structure des datasets à fournir

YOWO a été testé et validé sur des datasets comme UCF101-24, J-HMDB-21 et AVA, qui sont conçus pour la détection d’action spatio-temporelle. Les datasets doivent fournir :

- Des vidéos découpées en clips de N frames (souvent 8, 16 ou 32).
- Pour chaque frame clé, des annotations sous forme de bounding boxes et de labels d’action.
- Un fichier d’annotations (souvent au format `.json` ou `.csv`) qui relie chaque frame à ses bounding boxes et labels.
- Pour AVA, les annotations sont souvent fournies sous forme de fichiers CSV contenant le numéro de la vidéo, le timestamp, les coordonnées de la bounding box et le label d’action.

## Exemple de structure de fichier d’annotation

|Frame|x_min|y_min|x_max|y_max|Action_Label|
|---|---|---|---|---|---|
|video1/00001|34|60|80|120|5|
|video1/00002|35|62|82|122|5|

Les chemins des datasets et des annotations doivent être spécifiés dans les fichiers de configuration YAML du projet (ex : `ucf24.yaml`, `ava.yaml`).

## Exemple bref d’entraînement

Pour entraîner YOWO sur UCF101-24, il suffit de lancer la commande suivante après avoir préparé le dataset et téléchargé les poids pré-entraînés :
```bash
python main.py --cfg cfg/ucf24.yaml
```


Pour AVA :
```bash
python main.py --cfg cfg/ava.yaml
```

Toutes les configurations (chemins, hyperparamètres, etc.) sont définies dans les fichiers YAML correspondants. Après chaque époque, une évaluation automatique est réalisée et les métriques (frame-mAP, video-mAP) sont calculées.

## Différences entre YOWO v2 et v3

## YOWOv2

- Introduit une détection multi-niveaux (Feature Pyramid Network) pour gérer les actions à différentes échelles.
- Utilise un backbone 2D efficace combiné à un backbone 3D pour extraire les caractéristiques spatiales et temporelles.
- Adopte des stratégies modernes comme l’assignation dynamique des labels et un pipeline anchor-free pour la détection, ce qui améliore la précision et la simplicité du modèle.
- Propose plusieurs variantes (Nano, Tiny, Medium, Large) pour s’adapter aux contraintes de ressources et de performance.

## YOWOv3

- Repose sur un concept de « Two-Stream Network » avec une fusion optimisée des branches 2D et 3D.
- Améliore l’efficacité computationnelle : YOWOv3-L atteint des performances similaires à YOWOv2-L tout en réduisant de 26% la complexité (GLOPs) et de 45% le nombre de paramètres.
- Intègre un module de fusion attentionnel (CFAM) pour combiner efficacement les informations spatiales et temporelles.
- Utilise YOLOv8 comme extracteur de caractéristiques spatiales, ce qui offre une meilleure adaptabilité et des performances accrues.
- Les résultats montrent que YOWOv3 surpasse YOWOv2 en précision tout en étant plus léger et rapide.

|Modèle|mAP UCF101-24|mAP AVA v2.2|Paramètres|GLOPs|
|---|---|---|---|---|
|YOWOv2|85.2%|20.3%|109.7M|53.6|
|YOWOv3|88.3%|20.3%|59.8M|39.8|

En résumé, YOWOv3 est plus efficace et généralise mieux que YOWOv2, tout en étant plus léger et plus rapide pour la détection d’actions humaines dans les vidéos.