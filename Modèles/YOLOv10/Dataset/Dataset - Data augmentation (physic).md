---
tags:
  - recherches
  - programme
Date: 2025-05-21
References: "[[Bibliographie.canvas|Bibliographie]]"
Objectif: Ajouter de nouvelles données au dataset dans annoter de nouvelles images
aliases:
---
Pour générer physiquement un dataset augmenté (c’est-à-dire sauvegarder sur le disque chaque variante d’image augmentée). 
Voici un exemple simple de script Python utilisant la bibliothèque **Albumentations** pour augmenter physiquement un dataset déjà annoté au format YOLO : chaque image et son fichier d’annotation sont transformés ensemble, et les nouvelles images/annotations sont sauvegardées dans un nouveau dossier.

```python
import os
import cv2
import albumentations as A

# Dossiers d'entrée et de sortie
input_images = "images/"
input_labels = "labels/"
output_images = "aug_images/"
output_labels = "aug_labels/"
os.makedirs(output_images, exist_ok=True)
os.makedirs(output_labels, exist_ok=True)

# Définir les augmentations (exemple : flip horizontal + rotation)
transform = A.Compose([
    A.HorizontalFlip(p=1),
    A.Rotate(limit=20, p=1)
], bbox_params=A.BboxParams(format='yolo', label_fields=['class_labels']))

# Pour chaque image et annotation
for img_name in os.listdir(input_images):
    if not img_name.endswith('.jpg'):
        continue
    img_path = os.path.join(input_images, img_name)
    label_path = os.path.join(input_labels, img_name.replace('.jpg', '.txt'))

    # Charger image et annotations
    image = cv2.imread(img_path)
    h, w = image.shape[:2]
    bboxes = []
    class_labels = []
    with open(label_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            class_labels.append(int(parts[0]))
            bbox = list(map(float, parts[1:5]))
            bboxes.append(bbox)

    # Appliquer l’augmentation
    for i in range(3):  # nombre de variantes à générer
        augmented = transform(image=image, bboxes=bboxes, class_labels=class_labels)
        aug_img = augmented['image']
        aug_bboxes = augmented['bboxes']
        aug_labels = augmented['class_labels']

        # Sauvegarder l’image augmentée
        aug_img_name = img_name.replace('.jpg', f'_aug{i}.jpg')
        cv2.imwrite(os.path.join(output_images, aug_img_name), aug_img)

        # Sauvegarder l’annotation augmentée
        aug_label_name = aug_img_name.replace('.jpg', '.txt')
        with open(os.path.join(output_labels, aug_label_name), 'w') as f:
            for label, bbox in zip(aug_labels, aug_bboxes):
                f.write(f"{label} {' '.join(map(str, bbox))}\n")
```

Ce script lit chaque image et annotation, applique des augmentations (ici flip et rotation), et sauvegarde chaque variante avec son annotation adaptée. Les coordonnées des bounding boxes sont automatiquement recalculées pour rester cohérentes avec l’image transformée.

> [!tip]
> ON peut modifier les transformations et le nombre de variantes selon nos besoins.

