---
tags:
  - recherches
Date: 2025-05-23
References: "[[Bibliographie.canvas|Bibliographie]]"
Objectif: Explications
aliases:
  - anchor
  - anchor boxes
---
# Les Anchor Boxes dans la Détection d’Objet

Les _anchor boxes_ (ou boîtes d’ancrage) sont un concept fondamental utilisé dans la plupart des algorithmes modernes de détection d’objets, comme YOLO. Elles permettent de détecter efficacement plusieurs objets de tailles, formes et positions variées dans une image.

## Définition et Rôle
Une anchor box est une boîte englobante prédéfinie, caractérisée par une hauteur, une largeur et un rapport d’aspect spécifiques. Ces boîtes sont réparties à différents endroits de l’image, souvent selon une grille régulière. À chaque position de la grille, plusieurs anchor boxes de différentes tailles et proportions sont placées pour couvrir la diversité des objets à détecter.

L’objectif n’est pas de prédire directement la position exacte des objets, mais de partir de ces anchor boxes comme "suppositions initiales". Le réseau de neurones apprend ensuite à ajuster (raffiner) ces boîtes pour qu’elles s’alignent au mieux avec les objets réels présents dans l’image.

## Pourquoi des Anchor Boxes ?
Sans anchor boxes, il faudrait tester toutes les positions, tailles et formes possibles de boîtes, ce qui serait très coûteux (méthode du _sliding window_). 

![[ezgif.com-optimize--9-.gif]]
*Exemple of use of the sliding windows method*

Les anchor boxes, en étant prédéfinies et judicieusement choisies (souvent par clustering sur les annotations du jeu de données ou par un réseau de neurones), permettent de couvrir efficacement la diversité des objets tout en maintenant un calcul rapide et précis.

## Fonctionnement
Lors de l’inférence :
- Chaque image est découpée sous formes d'une grille
- À chaque case de la grille, le modèle associe une ou plusieurs anchor boxes. On peut avoir un type (forme ou taille) d'anchor box prédéfinis par classe.
- Pour chaque anchor box, le réseau prédit :
    - Une probabilité que la boîte contienne un objet d’une classe donnée.
    - Des ajustements (offsets) pour déplacer et redimensionner la boîte afin qu’elle corresponde mieux à l’objet détecté.
- Après ces prédictions, un filtrage (suppression non maximale, ou NMS) élimine les doublons et ne conserve que les boîtes les plus pertinentes.

![[Pasted image 20250523114330.png]]
*Exemple sur une détection de visage*


## Conclusion
Les anchor boxes sont donc des boîtes prédéfinies qui servent de point de départ à la détection d’objets dans les images. Leur utilisation est essentielle pour permettre aux réseaux de neurones de localiser et classifier efficacement de multiples objets, quelles que soient leurs dimensions ou leur positionnement dans l’image. Bien régler les anchor boxes selon les caractéristiques des objets à détecter est crucial pour obtenir de bonnes performances.