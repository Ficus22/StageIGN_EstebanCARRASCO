---
tags:
  - recherches
  - overview
Date: 2025-05-05
References: "[[Bibliographie.canvas|Bibliographie]]"
---
## Vue d'ensemble
La détection d'objets en temps réel vise à prédire avec précision les catégories et les positions des objets dans les images avec une faible latence. La série YOLO a été à l'avant-garde de cette recherche en raison de son équilibre entre performance et efficacité. Cependant, la dépendance à l'égard du NMS et les inefficacités architecturales ont empêché d'obtenir des performances optimales. YOLOv10 résout ces problèmes en introduisant des [affectations doubles cohérentes](https://arxiv.org/abs/2405.14458) pour une formation sans NMS et une stratégie de conception de modèle holistique axée sur l'efficacité et la précision.

### Architecture
L'architecture de YOLOv10 s'appuie sur les points forts des précédents modèles YOLO tout en introduisant plusieurs innovations clés. L'architecture du modèle se compose des éléments suivants :

1. **[Backbone](https://www.ultralytics.com/glossary/backbone)**: Responsable de l'[extraction des caractéristiques](https://www.ultralytics.com/glossary/feature-extraction), l'épine dorsale de YOLOv10 utilise une version améliorée de CSPNet (Cross Stage Partial Network) pour améliorer le flux de gradient et réduire la redondance des calculs.
2. Le **cou**: Le cou est conçu pour agréger les caractéristiques de différentes échelles et les transmettre à la tête. Il comprend des couches PAN (Path Aggregation Network) pour une fusion efficace des caractéristiques à plusieurs échelles.
3. **One-to-Many Head**: génère plusieurs prédictions par objet pendant la formation afin de fournir des signaux de supervision riches et d'améliorer la précision de l'apprentissage.
4. **One-to-One Head**: génère une seule meilleure prédiction par objet pendant l'inférence pour éliminer le besoin de NMS, réduisant ainsi la latence et améliorant l'efficacité.

## Caractéristiques principales

1. **Formation sans NMS**: Utilise des affectations doubles cohérentes pour éliminer le besoin de NMS, réduisant ainsi la [latence de l'inférence](https://www.ultralytics.com/glossary/inference-latency).
2. **Conception holistique du modèle**: Optimisation complète de divers composants du point de vue de l'efficacité et de la précision, y compris les têtes de classification légères, l'échantillonnage descendant découplé des canaux spatiaux et la conception de blocs guidés par les rangs.
3. **Amélioration des capacités du modèle**: Incorpore des [convolutions à](https://www.ultralytics.com/glossary/convolution) gros noyau et des modules d'auto-attention partielle pour améliorer les performances sans coût de calcul significatif.

## Variantes du modèle
YOLOv10 se décline en plusieurs modèles pour répondre aux différents besoins d'application :

- **YOLOv10n**: Version nano pour les environnements à ressources extrêmement limitées.
- **YOLOv10s**: Petite version équilibrant vitesse et précision.
- **YOLOv10m**: version moyenne à usage général.
- **YOLOv10b**: Version équilibrée avec une largeur accrue pour une plus grande précision.
- **YOLOv10l**: Grande version pour une plus grande précision au prix d'une augmentation des ressources informatiques.
- **YOLOv10x**: Version extra-large pour une précision et des performances maximales.

## Performance
YOLOv10 surpasse les versions précédentes de YOLO et d'autres modèles de pointe en termes de précision et d'efficacité. Par exemple, YOLOv10s est 1,8 fois plus rapide que [RT-DETR](https://docs.ultralytics.com/fr/models/rtdetr/) avec un AP similaire sur l'ensemble de données COCO, et YOLOv10b a 46 % de latence en moins et 25 % de paramètres en moins que [YOLOv9-C](https://docs.ultralytics.com/fr/models/yolov9/) avec la même performance.

### Détection (COCO)
Temps de latence mesuré avec TensorRT FP16 sur T4 GPU.

| Modèle                                                                                 | Taille de l'entrée | APval    | FLOPs (G) | Temps de latence (ms) |
| -------------------------------------------------------------------------------------- | ------------------ | -------- | --------- | --------------------- |
| [YOLOv10n](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov10n.pt) | 640                | 38.5     | **6.7**   | **1.84**              |
| [YOLOv10s](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov10s.pt) | 640                | 46.3     | 21.6      | 2.49                  |
| [YOLOv10m](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov10m.pt) | 640                | 51.1     | 59.1      | 4.74                  |
| [YOLOv10b](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov10b.pt) | 640                | 52.5     | 92.0      | 5.74                  |
| [YOLOv10l](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov10l.pt) | 640                | 53.2     | 120.3     | 7.28                  |
| [YOLOv10x](https://github.com/ultralytics/assets/releases/download/v8.3.0/yolov10x.pt) | 640                | **54.4** | 160.4     | 10.70                 |
## Méthodologie

### Affectations doubles cohérentes pour une formation sans NMS

YOLOv10 utilise une double attribution d'étiquettes, combinant les stratégies "one-to-many" et "one-to-one" pendant la formation afin de garantir une supervision riche et un déploiement efficace de bout en bout. La métrique de correspondance cohérente aligne la supervision entre les deux stratégies, améliorant ainsi la qualité des prédictions lors de l'[inférence](https://docs.ultralytics.com/fr/modes/predict/).

### Conception de modèles holistiques axés sur l'efficacité et la [précision](https://www.ultralytics.com/glossary/accuracy)

#### Amélioration de l'efficacité

1. **Tête de classification légère**: Réduit la charge de calcul de la tête de classification en utilisant des convolutions séparables en profondeur.
2. **Échantillonnage en aval découplé entre l'espace et le canal**: Découple la réduction spatiale et la modulation du canal pour minimiser la perte d'information et le coût de calcul.
3. **Conception de blocs guidée par les rangs**: Adapte la conception des blocs en fonction de la redondance intrinsèque des étages, garantissant ainsi une utilisation optimale des paramètres.

#### Amélioration de la précision

1. **Convolution à grand noyau**: Élargit le [champ réceptif](https://www.ultralytics.com/glossary/receptive-field) pour améliorer la capacité d'extraction des caractéristiques.
2. **Auto-attention partielle (PSA**) : incorpore des modules d'auto-attention pour améliorer l'apprentissage de la représentation globale avec un minimum de surcharge.

## Expériences et résultats

YOLOv10 a fait l'objet de tests approfondis sur des bancs d'essai standard tels que [COCO](https://docs.ultralytics.com/fr/datasets/detect/coco/), démontrant des performances et une efficacité supérieures. Le modèle obtient des résultats de pointe dans ses différentes variantes, et présente des améliorations significatives en termes de latence et de précision par rapport aux versions précédentes et à d'autres détecteurs contemporains.

## Exemples d'utilisation

Pour prédire de nouvelles images avec YOLOv10 :

```python
from ultralytics import YOLO

# Load a pre-trained YOLOv10n model
model = YOLO("yolov10n.pt")

# Perform object detection on an image
results = model("image.jpg")

# Display the results
results[0].show()
```

Pour l'entraînement de YOLOv10 sur un ensemble de données personnalisé :

```python
from ultralytics import YOLO

# Load YOLOv10n model from scratch
model = YOLO("yolov10n.yaml")

# Train the model
model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

## Conclusion
YOLOv10 établit une nouvelle norme en matière de détection d'objets en temps réel en remédiant aux lacunes des versions précédentes de YOLO et en intégrant des stratégies de conception innovantes. Sa capacité à fournir une grande précision avec un faible coût de calcul en fait un choix idéal pour un large éventail d'[applications réelles](https://www.ultralytics.com/solutions), notamment la [fabrication](https://www.ultralytics.com/solutions/ai-in-manufacturing), la [vente au détail](https://www.ultralytics.com/blog/ai-in-fashion-retail) et les [véhicules autonomes](https://www.ultralytics.com/solutions/ai-in-automotive).