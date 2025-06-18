---
tags:
  - recherches
  - programme
Date: 2025-05-21
References: "[[Bibliographie.canvas|Bibliographie]]"
Objectif: Ajouter de nouvelles données au dataset dans annoter de nouvelles images
aliases:
---

> [!info] Bibliothèque utilisée
> On pourrait utiliser plusieurs bibliothèques différentes pour procéder à de la data augmentation, comme notamment **PyTorch**, mais nous préfèrerons **YOLO** puisque nous l'utilisons déjà. 

## Introduction
L'augmentation des données est une technique cruciale en vision par ordinateur qui élargit artificiellement notre ensemble de données d'entraînement en appliquant diverses transformations aux images existantes. Lors de la formation de modèles d'apprentissage profond comme YOLO, l'augmentation des données permet d'améliorer la robustesse du modèle, de réduire le surajustement et d'améliorer la généralisation aux scénarios du monde réel.

### L'importance de l'augmentation des données
L'augmentation des données sert plusieurs objectifs essentiels dans la formation des modèles de vision par ordinateur :

- **Élargissement de l'ensemble de données : En créant des variantes d'images existantes, vous pouvez augmenter efficacement la taille de votre ensemble de données de formation sans collecter de nouvelles données.
- **Une meilleure généralisation : Les modèles apprennent à reconnaître des objets dans différentes conditions, ce qui les rend plus robustes dans les applications du monde réel.
- **Réduction du surajustement**: En introduisant de la variabilité dans les données d'apprentissage, les modèles sont moins susceptibles de mémoriser des caractéristiques d'image spécifiques.
- **Amélioration des performances : Les modèles formés avec une augmentation appropriée atteignent généralement une meilleure précision sur les ensembles de validation et de test.

L'implémentation d'Ultralytics YOLO fournit une suite complète de techniques d'augmentation, chacune servant des objectifs spécifiques et contribuant à la performance du modèle de différentes manières.


> [!tip] Utilisation d'un fichier de configuration
> Nous pouvons définir tous les paramètres de formation, y compris les augmentations, dans un fichier de configuration `.yaml` (par ex, `train_custom.yaml`). Ce nouveau fichier `.yaml` remplacera alors le fichier [celui par défaut](https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/default.yaml) situé dans le dossier `ultralytics`.
> ```yaml
> # train_custom.yaml
> mode: train
> data: coco8.yaml
> model: yolo11n.pt
> epochs: 100
> hsv_h: 0.03
> hsv_s: 0.6
> hsv_v: 0.5
> ```
> Pour lancer ensuite la formation avec le bon fichier de configuration 
> ```python
> from ultralytics import YOLO
> 
> model = YOLO("best.pt")
> 
> # Train the model with custom configuration
> model.train(cfg="train_custom.yaml")
> ```

> [!info]
> La data augmentation avec YOLOv10 ne crée pas un nombre fixe d’images supplémentaires dans le dossier de notre dataset : les augmentations sont appliquées « à la volée » pendant l’entraînement. Cela signifie que, pour un dataset de 100 images, le nombre d’images utilisées par epoch reste 100, mais chaque image peut être transformée différemment à chaque passage grâce aux techniques d’augmentation (flip, rotation, translation, etc.).
> Cependant on peut générer physiquement un dataset augmenté avec d'autres méthodes (*cf. [[Dataset - Data augmentation (physic)]]*)

## Augmentations de l'espace couleur

### Réglage de la teinte (`hsv_h`)

- **Gamme**: `0.0` - `1.0`
- **Défaut**: `0.015`
- **Utilisation**: modifie les couleurs de l'image tout en préservant leurs relations. Les couleurs de l'image `hsv_h` définit l'ampleur du décalage, l'ajustement final étant choisi de manière aléatoire entre `-hsv_h` et `hsv_h`. Par exemple, avec `hsv_h=0.3`, le quart est choisi au hasard à l'intérieur d'une fourchette de`-0.3` à `0.3`. Pour les valeurs supérieures à `0.5`Le changement de teinte s'étend autour de la roue chromatique, c'est pourquoi les augmentations sont les mêmes d'une couleur à l'autre. `0.5` et `-0.5`.
- **Objectif**: particulièrement utile pour les scénarios en extérieur où les conditions d'éclairage peuvent affecter considérablement l'apparence des objets. Par exemple, une banane peut paraître plus jaune en plein soleil, mais plus verte à l'intérieur.
- **Mise en œuvre d'Ultralytics**: [RandomHSV](https://docs.ultralytics.com/reference/data/augment/#ultralytics.data.augment.RandomHSV)

|**`-0.5`**|**`-0.25`**|**`0.0`**|**`0.25`**|**`0.5`**|
|---|---|---|---|---|
|![hsv_h_-0.5_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_hsv_h_-0.5.avif)|![hsv_h_-0.25_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_hsv_h_-0.25.avif)|![identité_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_identity.avif)|![hsv_h_0.25_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_hsv_h_0.25.avif)|![hsv_h_-0.5_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_hsv_h_0.5.avif)|

### Réglage de la saturation (`hsv_s`)

- **Gamme**: `0.0` - `1.0`
- **Défaut**: `0.7`
- **Utilisation**: modifie l'intensité des couleurs de l'image. L'intensité des couleurs de l'image est modifiée en fonction de la couleur de l'image. `hsv_h` définit l'ampleur du décalage, l'ajustement final étant choisi de manière aléatoire entre `-hsv_s` et `hsv_s`. Par exemple, avec `hsv_s=0.7`l'intensité est choisie au hasard dans`-0.7` à `0.7`.
- **Objectif**: aider les modèles à gérer les variations des conditions météorologiques et des réglages de la caméra. Par exemple, un panneau de signalisation rouge peut apparaître très vif par une journée ensoleillée, mais paraître terne et délavé par temps de brouillard.
- - **Mise en œuvre d'Ultralytics**: [RandomHSV](https://docs.ultralytics.com/reference/data/augment/#ultralytics.data.augment.RandomHSV)

| **`-1.0`**                                                                                                   | **`-0.5`**                                                                                                       | **`0.0`**                                                                                                    | **`0.5`**                                                                                                      | **`1.0`**                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| ![hsv_s_-1_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_hsv_s_-1.avif) | ![hsv_s_-0.5_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_hsv_s_-0.5.avif) | ![identité_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_identity.avif) | ![hsv_s_0.5_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_hsv_s_0.5.avif) | ![hsv_s_1_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_hsv_s_1.avif) |

### Réglage de la luminosité (`hsv_v`)

- **Gamme**: `0.0` - `1.0`
- **Défaut**: `0.4`
- **Utilisation**: modifie la luminosité de l'image. L'image `hsv_v` définit l'ampleur du décalage, l'ajustement final étant choisi de manière aléatoire entre `-hsv_v` et `hsv_v`. Par exemple, avec `hsv_v=0.4`l'intensité est choisie au hasard dans`-0.4` à `0.4`.
- **Objectif**: essentiel pour la formation des modèles qui doivent fonctionner dans des conditions d'éclairage différentes. Par exemple, une pomme rouge peut sembler brillante à la lumière du soleil, mais beaucoup plus sombre à l'ombre.
- **Mise en œuvre d'Ultralytics**: [RandomHSV](https://docs.ultralytics.com/reference/data/augment/#ultralytics.data.augment.RandomHSV)

|**`-1.0`**|**`-0.5`**|**`0.0`**|**`0.5`**|**`1.0`**|
|---|---|---|---|---|
|![hsv_v_-1_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_hsv_v_-1.avif)|![hsv_v_-0.5_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_hsv_v_-0.5.avif)|![identité_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_identity.avif)|![hsv_v_0.5_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_hsv_v_0.5.avif)|![hsv_v_1_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_hsv_v_1.avif)|

### Échange de canaux BGR (`bgr`)

- **Gamme**: `0.0` - `1.0`
- **Défaut**: `0.0`
- **Utilisation**: permet d'échanger les canaux de couleur d'une image de RVB à BGR, en modifiant l'ordre dans lequel les couleurs sont représentées. Les canaux `bgr` définit la probabilité d'appliquer la transformation, avec `bgr=1.0` en veillant à ce que toutes les images fassent l'objet d'un échange de canaux et `bgr=0.0` la désactiver. Par exemple, avec `bgr=0.5`chaque image a une chance sur deux d'être convertie de RVB en BGR.
- **Objectif**: Augmenter la robustesse aux différents ordres de canaux de couleur. Par exemple, lors de la formation de modèles qui doivent fonctionner avec différents systèmes de caméras et bibliothèques d'images où les formats RGB et BGR peuvent être utilisés de manière incohérente, ou lors du déploiement de modèles dans des environnements où le format de couleur d'entrée peut différer des données de formation.
- **Mise en œuvre d'Ultralytics**: [Format](https://docs.ultralytics.com/reference/data/augment/#ultralytics.data.augment.Format)

| **`bgr` éteint**                                                                                             | **`bgr` sur**                                                                                                        |
| ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| ![identité_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_identity.avif) | ![bgr_on_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_bgr_channel_swap_1.avif) |


## Transformations géométriques

### Rotation (`degrees`)

- **Gamme**: `0.0` à `180`
- **Défaut**: `0.0`
- **Utilisation**: Fait pivoter les images de manière aléatoire dans la plage spécifiée. Les images `degrees` définit l'angle de rotation, l'ajustement final étant choisi de manière aléatoire entre `-degrees` et `degrees`. Par exemple, avec `degrees=10.0`la rotation est choisie au hasard dans les limites de`-10.0` à `10.0`.
- **Objectif**: essentiel pour les applications dans lesquelles les objets peuvent apparaître dans des orientations différentes. Par exemple, dans l'imagerie aérienne par drone, les véhicules peuvent être orientés dans n'importe quelle direction, ce qui exige que les modèles reconnaissent les objets indépendamment de leur rotation.
- **Mise en œuvre d'Ultralytics**: [RandomPerspective](https://docs.ultralytics.com/reference/data/augment/#ultralytics.data.augment.RandomPerspective)

|**`-180`**|**`-90`**|**`0.0`**|**`90`**|**`180`**|
|---|---|---|---|---|
|![degrés_-180_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_degrees_-180.avif)|![degrés_-90_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_degrees_-90.avif)|![identité_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_identity.avif)|![degrés_90_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_degrees_90.avif)|![degrés_180_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_degrees_180.avif)|


### Traduction (`translate`)

- **Gamme**: `0.0` - `1.0`
- **Défaut**: `0.1`
- **Utilisation**: décale les images horizontalement et verticalement d'une fraction aléatoire de la taille de l'image. La fonction `translate` définit l'ampleur du décalage, l'ajustement final étant choisi aléatoirement deux fois (une fois pour chaque axe) dans l'intervalle `-translate` et `translate`. Par exemple, avec `translate=0.5`la traduction est choisie de manière aléatoire à l'intérieur d'une fourchette de`-0.5` à `0.5` sur l'axe des x, et une autre valeur aléatoire indépendante est sélectionnée dans le même intervalle sur l'axe des y.
- **Objectif**: aider les modèles à apprendre à détecter des objets partiellement visibles et améliorer la résistance à la position de l'objet. Par exemple, dans les applications d'évaluation des dommages subis par les véhicules, les pièces de la voiture peuvent apparaître entièrement ou partiellement dans le cadre en fonction de la position et de la distance du photographe ; l'augmentation de la traduction apprendra au modèle à reconnaître ces caractéristiques indépendamment de leur intégralité ou de leur position.
- **Mise en œuvre d'Ultralytics**: [RandomPerspective](https://docs.ultralytics.com/reference/data/augment/#ultralytics.data.augment.RandomPerspective)

> [!NOTE]
> Par souci de simplicité, les traductions appliquées ci-dessous sont les mêmes à chaque fois pour les deux `x` et `y` axes. Valeurs `-1.0` et `1.0`ne sont pas représentées car elles feraient sortir complètement l'image du cadre.

|`-0.5`|**`-0.25`**|**`0.0`**|**`0.25`**|**`0.5`**|
|---|---|---|---|---|
|![translate_-0.5_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_translate_-0.5.avif)|![translate_-0.25_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_translate_-0.25.avif)|![identité_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_identity.avif)|![translate_0.25_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_translate_0.25.avif)|![translate_0.5_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_translate_0.5.avif)|

### Échelle (`scale`)

- **Gamme**: ≥`0.0`
- **Défaut**: `0.5`
- **Utilisation**: redimensionne les images par un facteur aléatoire dans la plage spécifiée. La fonction `scale` définit le facteur d'échelle, l'ajustement final étant choisi de manière aléatoire entre `1-scale` et `1+scale`. Par exemple, avec `scale=0.5`le cadrage est choisi au hasard à l'intérieur de`0.5` à `1.5`.
- **Objectif**: permettre aux modèles de traiter des objets de distances et de tailles différentes. Par exemple, dans les applications de conduite autonome, les véhicules peuvent apparaître à différentes distances de la caméra, ce qui oblige le modèle à les reconnaître quelle que soit leur taille.
- **Mise en œuvre d'Ultralytics**: [RandomPerspective](https://docs.ultralytics.com/reference/data/augment/#ultralytics.data.augment.RandomPerspective)

> [!NOTE]
>    - La valeur `-1.0` n'est pas affichée car elle ferait disparaître l'image, tandis que `1.0` se traduit simplement par un zoom 2x.
>    - Les valeurs affichées dans le tableau ci-dessous sont celles appliquées par l'intermédiaire de l'hyperparamètre `scale`et non le facteur d'échelle final.
>    - Si `scale` est supérieur à `1.0`l'image peut être soit très petite, soit inversée, car le facteur d'échelle est choisi au hasard entre `1-scale` et `1+scale`. Par exemple, avec `scale=3.0`le cadrage est choisi au hasard à l'intérieur de`-2.0` à `4.0`. Si une valeur négative est choisie, l'image est retournée.

|**`-0.5`**|**`-0.25`**|**`0.0`**|**`0.25`**|**`0.5`**|
|---|---|---|---|---|
|![échelle_-0.5_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_scale_-0.5.avif)|![échelle_-0.25_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_scale_-0.25.avif)|![identité_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_identity.avif)|![échelle_0.25_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_scale_0.25.avif)|![échelle_0.5_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_scale_0.5.avif)|

### Cisaillement (`shear`)

- **Gamme**: `-180` à `+180`
- **Défaut**: `0.0`
- **Utilisation**: introduit une transformation géométrique qui incline l'image le long des axes x et y, déplaçant ainsi des parties de l'image dans une direction tout en conservant des lignes parallèles. La transformation `shear` définit l'angle de cisaillement, l'ajustement final étant choisi de manière aléatoire entre `-shear` et `shear`. Par exemple, avec `shear=10.0`le cisaillement est choisi au hasard à l'intérieur de`-10` à `10` sur l'axe des x, et une autre valeur aléatoire indépendante est sélectionnée dans le même intervalle sur l'axe des y.
- **Objectif**: aider les modèles à s'adapter aux variations des angles de vue causées par de légères inclinaisons ou des points de vue obliques. Par exemple, dans le cadre de la surveillance du trafic, les objets tels que les voitures et les panneaux de signalisation peuvent apparaître inclinés en raison de l'emplacement non perpendiculaire des caméras. L'application de l'augmentation du cisaillement permet au modèle d'apprendre à reconnaître les objets malgré ces distorsions obliques.
- **Mise en œuvre d'Ultralytics**: [RandomPerspective](https://docs.ultralytics.com/reference/data/augment/#ultralytics.data.augment.RandomPerspective)

> [!NOTE]
> - `shear` peuvent rapidement déformer l'image, il est donc recommandé de commencer par de petites valeurs et de les augmenter progressivement.
> - Contrairement aux transformations de la perspective, le cisaillement n'introduit pas de profondeur ou de points de fuite, mais déforme la forme des objets en modifiant leurs angles tout en conservant les côtés opposés parallèles.

|**`-10`**|**`-5`**|**`0.0`**|**`5`**|**`10`**|
|---|---|---|---|---|
|![cisaillement_-10_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_shear_-10.avif)|![cisaillement_-5_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_shear_-5.avif)|![identité_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_identity.avif)|![cisaillement_5_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_shear_5.avif)|![cisaillement_10_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_shear_10.avif)|

### Perspective (`perspective`)

- **Gamme**: `0.0` - `0.001`
- **Défaut**: `0.0`
- **Utilisation**: applique une transformation complète de la perspective le long des axes x et y, simulant la façon dont les objets apparaissent lorsqu'ils sont vus à différentes profondeurs ou sous différents angles. L'image `perspective` définit l'ampleur de la perspective, l'ajustement final étant choisi aléatoirement entre `-perspective` et `perspective`. Par exemple, avec `perspective=0.001`la perspective est choisie au hasard dans les limites de`-0.001` à `0.001` sur l'axe des x, et une autre valeur aléatoire indépendante est sélectionnée dans le même intervalle sur l'axe des y.
- **Objectif**: L'augmentation de la perspective est cruciale pour gérer les changements extrêmes de point de vue, en particulier dans les scénarios où les objets apparaissent raccourcis ou déformés en raison des changements de perspective. Par exemple, dans la détection d'objets par drone, les bâtiments, les routes et les véhicules peuvent apparaître étirés ou comprimés en fonction de l'inclinaison et de l'altitude du drone. En appliquant des transformations de perspective, les modèles apprennent à reconnaître les objets malgré ces distorsions induites par la perspective, ce qui améliore leur robustesse dans les déploiements réels.
- **Mise en œuvre d'Ultralytics**: [RandomPerspective](https://docs.ultralytics.com/reference/data/augment/#ultralytics.data.augment.RandomPerspective)

|**`-0.001`**|**`-0.0005`**|**`0.0`**|**`0.0005`**|**`0.001`**|
|---|---|---|---|---|
|![perspective_-0.001_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_perspective_-0.001.avif)|![perspective_-0.0005_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_perspective_-0.0005.avif)|![identité_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_identity.avif)|![perspective_0.0005_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_perspective_0.0005.avif)|![perspective_0.001_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_geometric_perspective_0.001.avif)|

### Basculer de haut en bas (`flipud`)

- **Gamme**: `0.0` - `1.0`
- **Défaut**: `0.0`
- **Utilisation**: effectue un retournement vertical en inversant l'image le long de l'axe des ordonnées. Cette transformation renvoie l'image entière à l'envers mais préserve toutes les relations spatiales entre les objets. L'hyperparamètre flipud définit la probabilité d'appliquer la transformation, avec une valeur de `flipud=1.0` en veillant à ce que toutes les images soient inversées et à ce qu'une valeur de `flipud=0.0` la désactivation totale de la transformation. Par exemple, avec `flipud=0.5`chaque image a une chance sur deux d'être retournée.
- **Objectif**: utile pour les scénarios dans lesquels les objets peuvent apparaître à l'envers. Par exemple, dans les systèmes de vision robotique, les objets sur les tapis roulants ou les bras robotiques peuvent être saisis et placés dans différentes orientations. Le retournement vertical aide le modèle à reconnaître les objets indépendamment de leur positionnement de haut en bas.
- **Mise en œuvre d'Ultralytics**: [RandomFlip](https://docs.ultralytics.com/reference/data/augment/#ultralytics.data.augment.RandomFlip)

|**`flipud` éteint**|**`flipud` sur**|
|---|---|
|![identité_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_identity.avif)|![flipud_on_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_flip_vertical_1.avif)|

### Inversion gauche-droite (`fliplr`)

- **Gamme**: `0.0` - `1.0`
- **Défaut**: `0.5`
- **Utilisation**: effectue un retournement horizontal en reflétant l'image le long de l'axe x. Cette transformation intervertit les côtés gauche et droit tout en maintenant la cohérence spatiale, ce qui aide le modèle à se généraliser aux objets apparaissant dans des orientations inversées. Le modèle `fliplr` définit la probabilité d'appliquer la transformation, avec une valeur de `fliplr=1.0` en veillant à ce que toutes les images soient inversées et à ce qu'une valeur de `fliplr=0.0` disabling the transformation entirely. For example, with `fliplr=0.5`chaque image a une chance sur deux d'être retournée de gauche à droite.
- **Objectif**: Le retournement horizontal est largement utilisé dans la détection d'objets, l'estimation de la pose et la reconnaissance faciale afin d'améliorer la robustesse contre les variations gauche-droite. Par exemple, dans la conduite autonome, les véhicules et les piétons peuvent apparaître d'un côté ou de l'autre de la route, et le retournement horizontal permet au modèle de les reconnaître aussi bien dans les deux orientations.
- **Mise en œuvre d'Ultralytics**: [RandomFlip](https://docs.ultralytics.com/reference/data/augment/#ultralytics.data.augment.RandomFlip)

|**`fliplr` éteint**|**`fliplr` sur**|
|---|---|
|![identité_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_identity.avif)|![fliplr_on_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_flip_horizontal_1.avif)|

### Mosaïque (`mosaic`)

- **Gamme**: `0.0` - `1.0`
- **Défaut**: `1.0`
- **Utilisation**: Combine quatre images d'apprentissage en une seule. L'image `mosaic` définit la probabilité d'appliquer la transformation, avec `mosaic=1.0` en veillant à ce que toutes les images soient combinées et `mosaic=0.0` la désactivation de la transformation. Par exemple, avec `mosaic=0.5`Chaque image a une chance sur deux d'être combinée avec trois autres images.
- **Objectif**: très efficace pour améliorer la détection des petits objets et la compréhension du contexte. Par exemple, dans les projets de conservation de la faune où les animaux peuvent apparaître à différentes distances et échelles, l'augmentation de la mosaïque aide le modèle à apprendre à reconnaître la même espèce à travers différentes tailles, occlusions partielles et contextes environnementaux en créant artificiellement divers échantillons d'entraînement à partir de données limitées.
- La **mise en œuvre d'Ultralytics**: [Mosaic](https://docs.ultralytics.com/reference/data/augment/#ultralytics.data.augment.Mosaic)

> [!NOTE]
> - Même si le `mosaic` rend le modèle plus robuste, elle peut également rendre le processus de formation plus difficile.
> - Le `mosaic` peut être désactivée vers la fin de la formation en réglant le paramètre `close_mosaic` au nombre d'époques avant la fin de l'opération, au moment où elle doit être désactivée. Par exemple, si `epochs` est fixé à `200` et `close_mosaic` est fixé à `20`, le `mosaic` sera désactivée après que l'augmentation de la `180` époques. Si les `close_mosaic` est fixé à `0`, le `mosaic` sera activé tout au long du processus de formation.
> - Le centre de la mosaïque générée est déterminé à l'aide de valeurs aléatoires et peut se trouver à l'intérieur ou à l'extérieur de l'image.
> - La mise en œuvre actuelle de la `mosaic` combine 4 images choisies au hasard dans l'ensemble de données. Si l'ensemble de données est petit, la même image peut être utilisée plusieurs fois dans la même mosaïque.

|**`mosaic` éteint**|**`mosaic` sur**|
|---|---|
|![identité_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_identity.avif)|![mosaïque_sur_augmentation](https://github.com/ultralytics/docs/releases/download/0/augmentation_mosaic_on.avif)|

## Quelles augmentations choisir ?

> [!question]
> Le choix des bonnes augmentations dépend de notre cas d'utilisation spécifique et de notre ensemble de données. 
> 
> - Dans la plupart des cas, de légères variations de couleur et de luminosité sont bénéfiques. Les valeurs par défaut de `hsv_h`, `hsv_s`et `hsv_v` constituent un bon point de départ.
> - Si le point de vue de la caméra est cohérent et ne changera pas une fois le modèle déployé, on peut probablement ignorer les transformations géométriques telles que `rotation`, `translation`, `scale`, `shear`ou `perspective`. Cependant, si l'angle de la caméra peut varier et que le modèle doit être plus robuste, il est préférable de conserver ces augmentations.
> - Utiliser le `mosaic` uniquement si la présence d'objets partiellement occultés ou de plusieurs objets par image est acceptable et ne modifie pas la valeur de l'étiquette. Il est également possible de conserver `mosaic` actifs mais augmentent la `close_mosaic` pour le désactiver plus tôt dans le processus de formation.
> 
> En bref : restons simple. Commencez par un petit ensemble d'augmentations et ajoutons-en progressivement si nécessaire. L'objectif est d'améliorer la généralisation et la robustesse du modèle, et non de compliquer à l'excès le processus de formation. Nous devons aussi nous assurer que les augmentations que l'on applique reflètent la même distribution de données que celle à laquelle notre modèle sera confronté en production.

