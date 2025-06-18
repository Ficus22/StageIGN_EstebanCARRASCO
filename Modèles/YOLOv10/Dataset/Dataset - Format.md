---
tags:
  - recherches
Date: 2025-05-06
References: "[[Bibliographie.canvas|Bibliographie]]"
---
Les modèles YOLOv5 nécessitent des données étiquetées pour apprendre les caractéristiques visuelles des classes d'objets. Il est essentiel d'organiser correctement votre ensemble de données.

### 1 Créer `dataset.yaml`

Le fichier de configuration du jeu de données (par exemple, `coco128.yaml`) décrit la structure de l'ensemble de données, les noms des classes et les chemins d'accès aux répertoires d'images. [COCO128](https://docs.ultralytics.com/fr/datasets/detect/coco128/) sert de petit ensemble de données d'exemple, comprenant les 128 premières images de la base de données extensive. [COCO](https://docs.ultralytics.com/fr/datasets/detect/coco/) . Il est utile pour tester rapidement le pipeline de formation et diagnostiquer des problèmes potentiels tels que [surajustement](https://www.ultralytics.com/glossary/overfitting).

Le `dataset.yaml` comprend la structure du fichier :

- `path`: Le répertoire racine contenant le jeu de données.
- `train`, `val`, `test`: Chemins relatifs de `path` vers des répertoires contenant des images ou des fichiers texte répertoriant les chemins d'accès aux images pour les ensembles d'apprentissage, de validation et de test.
- `names`: Un dictionnaire établissant une correspondance entre les indices des classes (à partir de 0) et les noms des classes correspondantes.

Vous trouverez ci-dessous la structure de `coco128.yaml` ([voir sur GitHub](https://github.com/ultralytics/yolov5/blob/master/data/coco128.yaml)) :
```yaml
# Dataset root directory relative to the yolov5 directory
path: ../datasets/coco128

# Train/val/test sets: specify directories, *.txt files, or lists
train: images/train2017 # 128 images for training
val: images/train2017 # 128 images for validation
test: # Optional path to test images

# Classes (example using 80 COCO classes)
names:
    0: person
    1: bicycle
    2: car
    # ... (remaining COCO classes)
    77: teddy bear
    78: hair drier
    79: toothbrush
```

### 2 Exploiter les modèles pour l'étiquetage automatisé

Bien que l'étiquetage manuel à l'aide d'outils soit une approche courante, le processus peut prendre beaucoup de temps. Les progrès récents des modèles de fondation offrent des possibilités d'automatisation ou de semi-automatisation du processus d'annotation, ce qui peut accélérer considérablement la création d'ensembles de données. Voici quelques exemples de modèles qui peuvent aider à générer des étiquettes :

- **[Google Gemini](https://colab.research.google.com/github/ultralytics/notebooks/blob/main/notebooks/how-to-use-google-gemini-models-for-object-detection-image-captioning-and-ocr.ipynb)**: Les grands modèles multimodaux comme Gemini possèdent de puissantes capacités de compréhension des images. Ils peuvent être invités à identifier et à localiser des objets dans des images, en générant des boîtes de délimitation ou des descriptions qui peuvent être converties en étiquettes au format YOLO . Explorez son potentiel dans le carnet de notes fourni.
- **[SAM2 (Segment Anything Model 2)](https://docs.ultralytics.com/fr/models/sam-2/)**: Les modèles de fondation axés sur la segmentation, comme SAM2, peuvent identifier et délimiter des objets avec une grande précision. Bien qu'ils soient principalement destinés à la segmentation, les masques obtenus peuvent souvent être convertis en annotations de boîtes de délimitation adaptées aux tâches de détection d'objets.
- **[YOLOWorld](https://docs.ultralytics.com/fr/models/yolo-world/)**: Ce modèle offre des capacités de détection à partir d'un vocabulaire ouvert. Vous pouvez fournir des descriptions textuelles des objets qui vous intéressent, et YOLOWorld peut les localiser dans les images _sans_ formation préalable sur ces classes spécifiques. Cela peut être utilisé comme point de départ pour générer des étiquettes initiales, qui peuvent ensuite être affinées.

L'utilisation de ces modèles peut constituer une étape de "pré-étiquetage", réduisant l'effort manuel nécessaire. Cependant, il est essentiel de revoir et d'affiner les étiquettes générées automatiquement afin d'en garantir l'exactitude et la cohérence, car la qualité a un impact direct sur les performances de votre modèle YOLOv5 entraîné. Après avoir généré (et éventuellement affiné) vos étiquettes, assurez-vous qu'elles respectent la norme **YOLO format**: un `*.txt` par image, chaque ligne représentant un objet en tant que `class_index x_center y_center width height` (coordonnées normalisées, classe zéro). Si une image ne contient pas d'objets intéressants, aucun objet correspondant n'a été identifié. `*.txt` est nécessaire.

Le format YOLO `*.txt` les spécifications des fichiers sont précises :

- Une ligne par [boîte de délimitation de l'](https://www.ultralytics.com/glossary/bounding-box)objet.
- Chaque ligne doit contenir `class_index x_center y_center width height`.
- Les coordonnées doivent être **normalisé** à une valeur comprise entre 0 et 1. Pour ce faire, divisez les valeurs des pixels de `x_center` et `width` par la largeur totale de l'image, et diviser `y_center` et `height` par la hauteur totale de l'image.
- Les indices de classe sont indexés par zéro (c'est-à-dire que la première classe est représentée par `0`, le second par `1`et ainsi de suite).

![[RepérageDesCoordonnées.png]]

Le fichier d'étiquettes correspondant à l'image ci-dessus, contenant deux objets "personne" (indice de classe `0`) et un objet "cravate" (indice de classe `27`), ressemblerait à ceci :
```text
0  0.481719 0.634028 0.690625 0.713278
0  0.741094 0.524306 0.314750 0.933389
27 0.364844 0.795833 0.078125 0.400000
```

### 3 Organiser les répertoires

Structurez votre [ensembles de données](https://docs.ultralytics.com/fr/datasets/) comme illustré ci-dessous. Par défaut, YOLOv5 anticipe le répertoire du jeu de données (par exemple, `/coco128`) de résider à l'intérieur d'un `/datasets` dossier situé **adjacente à** les `/yolov5` dans le répertoire du dépôt.

YOLOv5 localise automatiquement les étiquettes pour chaque image en substituant la dernière instance de `/images/` dans le chemin de l'image avec `/labels/`. Par exemple :
```
../datasets/coco128/images/im0.jpg # Path to the image file
../datasets/coco128/labels/im0.txt # Path to the corresponding label file
```

La structure de répertoire recommandée est la suivante
```
/datasets/
└── coco128/  # Dataset root
    ├── images/
    │   ├── train2017/  # Training images
    │   │   ├── 000000000009.jpg
    │   │   └── ...
    │   └── val2017/    # Validation images (optional if using same set for train/val)
    │       └── ...
    └── labels/
        ├── train2017/  # Training labels
        │   ├── 000000000009.txt
        │   └── ...
        └── val2017/    # Validation labels (optional if using same set for train/val)
            └── ...
```


