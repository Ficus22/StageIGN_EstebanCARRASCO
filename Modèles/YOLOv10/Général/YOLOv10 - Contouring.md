---
tags:
  - recherches
Date: 2025-05-05
References: "[[Bibliographie.canvas|Bibliographie]]"
Objectif: Savoir si l'on peut avoir un détourage plus précis qu'un carré englobant
---
Avec YOLOv10, la sortie standard du modèle est une boîte englobante (bounding box) qui encadre l'objet détecté, et non le contour précis de la forme de l'objet. YOLOv10, comme les autres versions de YOLO, est conçu principalement pour la détection d'objets sous forme de rectangles alignés sur les axes, ce qui signifie que la sortie est typiquement une bounding box avec ses coordonnées (exemple : format XYXY ou XYWH).

YOLOv10 n'intègre pas nativement une fonctionnalité de segmentation d'instance ou de contour précis (masque) comme le ferait un modèle de type Mask R-CNN ou une version spécialisée de YOLO pour la segmentation (par exemple YOLOv8 Segmentation). Sa sortie reste donc limitée à la localisation par rectangles.

Si vous souhaitez obtenir le contour exact de la forme détectée plutôt qu'une simple boîte, il faudrait envisager une approche complémentaire, telle que :

- Utiliser un modèle de segmentation d'instance ou de segmentation sémantique qui fournit des masques binaires correspondant aux objets détectés.
- Combiner YOLOv10 pour la détection rapide des objets avec un modèle de segmentation pour extraire les contours précis.
- Appliquer des techniques post-traitement sur l'image (ex. segmentation par contours, extraction de contours à partir de masques) si vous avez un masque.

En résumé, YOLOv10 ne fournit pas directement le contour de la forme détectée, mais uniquement la bounding box. Pour obtenir un contour précis, il faut utiliser un modèle de segmentation ou une méthode complémentaire à YOLOv10.

**Synthèse :**

- YOLOv10 produit en sortie des bounding boxes (rectangles) autour des objets détectés.
- Il ne fournit pas directement les contours précis des formes détectées.
- Pour avoir les contours, il faut utiliser un modèle de segmentation ou un traitement complémentaire.
- YOLOv10 est optimisé pour la détection rapide avec des boîtes, pas pour la segmentation.