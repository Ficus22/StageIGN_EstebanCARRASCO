---
tags:
  - "#recherches"
  - "#overview"
Date: 2025-05-07
References: "[[Bibliographie.canvas|Bibliographie]]"
aliases:
  - DLC Overview
---
>**DeepLabCut™** is an efficient method for 2D and 3D marker less pose estimation based on transfer learning with deep neural networks that achieves excellent results (i.e. you can match human labelling accuracy) with minimal training data (typically 50-200 frames). We demonstrate the versatility of this framework by tracking various body parts in multiple species across a broad collection of behaviours. The package is open source, fast, robust, and [can be used to compute 3D pose](https://www.nature.com/articles/s41596-019-0176-0) estimates or [for multi-animals](https://www.biorxiv.org/content/10.1101/2021.04.30.442096v1). Please see the original paper and the latest work below! This package is collaboratively developed by the [Mathis Group](https://www.mathislab.org/) & [Mathis Lab](https://www.mackenziemathislab.org/home) at EPFL (releases prior to 2.1.9 were developed at Harvard University).

*Extrait de la page d'acceuil du site DeepLabCut, cf. [[Bibliographie.canvas|Bibliographie]]*

DeepLabCut est une boîte à outils open-source de pose estimation qui utilise des réseaux de neurones profonds (Deep Learning) pour suivre des points clés sur des animaux (ou humains) dans des images ou des vidéos.  
Elle repose sur des architectures de **DeepCut** et de **ResNet**, adaptées pour un entraînement efficace avec peu d’annotations.

L'objectif principale, est de suivre automatiquement les parties du corps d’un animal (ou plusieurs animaux), à partir de quelques annotations manuelles seulement.

## **Principales caractéristiques**

| FONCTIONNALITE                          | DESCRIPTION                                                                                     |
| --------------------------------------- | ----------------------------------------------------------------------------------------------- |
| **Multi-espèces**                       | Fonctionne avec presque tous les animaux (rongeurs, oiseaux, poissons, insectes, humains, etc.) |
| **Basé sur ResNet**                     | Utilise ResNet50/101/152 ou MobileNet pour l’extraction de caractéristiques                     |
| **Entraînement avec peu de données**    | Excellente performance avec seulement ~100 images annotées                                      |
| **Analyse vidéo**                       | Analyse des vidéos pour générer des trajectoires précises des points clés                       |
| **Visualisation intégrée**              | Création de vidéos étiquetées et de tracés pour les trajectoires                                |
| **Multi-individu (avec DeepLabCut-MA)** | Possibilité de suivre plusieurs individus (extension récente)                                   |

## **Pipeline typique**

1. Création du projet  
2. Annotation manuelle de quelques frames  
3. Entraînement du modèle  
4. Évaluation du modèle  
5. Analyse de vidéos complètes  
6. Filtrage et visualisation des données  


## **Cas d’usage courants**

- Analyse du comportement animal en neurosciences
- Suivi de mouvement chez les insectes
- Analyse de la locomotion (rongeurs, chevaux, humains, etc.)
- Biomécanique et étude posturale
- Suivi en environnement naturel (caméra trappe, drone, etc.)


##  **Technologies utilisées**

- Python
- TensorFlow / Keras
- OpenCV pour la vidéo
- Support GPU via CUDA (pour l'entraînement accéléré)

