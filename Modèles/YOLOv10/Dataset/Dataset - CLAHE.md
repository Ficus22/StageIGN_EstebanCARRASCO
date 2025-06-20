---
tags:
  - recherches
Date: 2025-06-17
References: "[[Bibliographie.canvas|Bibliographie]]"
Objectif: Améliorer la qualité des images
aliases:
---
CLAHE (Contrast Limited Adaptive Histogram Equalization) est une méthode avancée pour améliorer le contraste des images, particulièrement efficace lorsque l’image présente des zones d’éclairage inégal. Contrairement à l’égalisation d’histogramme globale, qui applique la même transformation à toute l’image, CLAHE divise l’image en petites régions (appelées _tiles_) et ajuste le contraste localement dans chacune d’elles. Cela permet d’améliorer la visibilité des détails dans les zones sombres comme dans les zones claires, tout en limitant l’amplification du bruit grâce au paramètre de _clip limit_.

## Fonctionnement de CLAHE
zation) est une méthode avancée pour améliorer le contraste des images, particulièr
- **Division en tiles** : L’image est découpée en une grille de régions rectangulaires (par exemple, 8x8).
- **Égalisation locale** : Un histogramme est calculé pour chaque tile, puis une égalisation locale est appliquée.
- **Limitation du contraste** (_clip limit_) : Pour éviter d’amplifier le bruit dans les zones homogènes, la contribution maximale d’un bin de l’histogramme est limitée. L’excès est redistribué.
- **Fusion douce** : Les bords entre les tiles sont lissés pour éviter les artefacts.

## Utilisation de CLAHE avec OpenCV (Python)

Voici comment appliquer CLAHE à une image avec OpenCV :
```python
import cv2 

# Charger l'image et la convertir en niveaux de gris 
image = cv2.imread('image.jpg') 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

# Créer l'objet CLAHE avec les paramètres souhaités 
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)) 

# Appliquer CLAHE 
equalized = clahe.apply(gray) 

# Afficher le résultat 
cv2.imshow('CLAHE', equalized) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
```

- **clipLimit** : Limite l’amplification du contraste (valeur typique : 2.0). Plus il est élevé, plus le contraste est fort, mais attention au bruit.
- **tileGridSize** : Nombre de tiles en largeur et hauteur (par exemple, (8, 8)). Plus les tiles sont petits, plus la correction est locale.

## Pour les images couleur

Il est recommandé d’appliquer CLAHE uniquement sur la composante de luminance (par exemple, canal L de l’espace LAB), puis de reconstituer l’image couleur:

```python
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB) 
l, a, b = cv2.split(lab) 
cl = clahe.apply(l) 
limg = cv2.merge((cl, a, b)) 
final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
```

## Points forts de CLAHE

- Améliore le contraste localement, idéal pour les images à éclairage non uniforme.
- Limite l’amplification du bruit grâce au paramètre _clip limit_.
- Très utilisé en imagerie médicale, vision nocturne et traitement d’images scientifiques.

## Conseils

- Ajuste `clipLimit` et `tileGridSize` selon l’aspect visuel souhaité et la taille de ton image.
- Pour éviter des artefacts, commence avec les valeurs par défaut (clipLimit=2.0, tileGridSize=(8,8)) puis affine selon le résultat.


En résumé, CLAHE est la méthode de référence pour améliorer dynamiquement et localement le contraste d’images hétérogènes, et son implémentation OpenCV est simple et efficace.