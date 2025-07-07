---
tags:
  - recherches
  - programme
Date: 2025-07-04
References: "[[Bibliographie.canvas|Bibliographie]]"
Objectif: Déterminer une bonne metric d'évaluation des performance d'un modèle
aliases:
---
## Récupération de l'image inférrée
Pour récupérer le fichier `.txt` des labels générés par YOLO après inférence sur une image, il existe une méthode standard intégrée dans les outils Ultralytics  :

```python
from ultralytics import YOLO
	model = YOLO("yolo11n.pt")
	
results = model("path/to/image.jpg")
for result in results:
     result.save_txt("output.txt")
```
*extrait de la [doc ultralytics](https://docs.ultralytics.com/reference/engine/results/#ultralytics.engine.results.Results.save_txt)*

Cela dit peut-être qu'une utilisation direct sous forme de dataframe est plus optimale.

## Métrique faite maison
### 1. Nombre d’individus détectés (25 points)

- **But** : Évaluer l’écart absolu entre le nombre d’abeilles détectées et le nombre réel.
- **Notation** : 25/25 si le nombre est exact, score décroissant linéairement jusqu’à 0/25 si l’écart atteint 50 %.

### 2. Erreur de localisation des bounding boxes (IoU moyen) (25 points)

- **But** : Mesurer la précision de la localisation.
- **Notation** : 25/25 si IoU moyen ≥ 0,85, linéairement décroissant jusqu’à 0/25 si IoU ≤ 0,5.

### 3. Précision (10 points)

- **But** : Proportion de détections correctes parmi toutes les détections.
- **Notation** : 10/10 si précision ≥ 0,95, linéairement jusqu’à 0/10 si précision ≤ 0,7.

### 4. Rappel (10 points)

- **But** : Proportion d’abeilles détectées parmi toutes les abeilles présentes.
- **Notation** : 10/10 si rappel ≥ 0,95, linéairement jusqu’à 0/10 si rappel ≤ 0,7.

### 5. mAP@0.5 (10 points)

- **But** : Performance globale des détections.
- **Notation** : 10/10 si mAP@0.5 ≥ 0,95, linéairement jusqu’à 0/10 si mAP@0.5 ≤ 0,7.

### 6. Temps d’inférence (10 points)

- **But** : Évaluer la rapidité du modèle.
- **Notation** : 10/10 si < 100 ms, linéairement décroissant jusqu’à 0/10 si > 1 s.

### 7. Taux de faux positifs (FPR – 10 points)

- **But** : Évaluer la pureté des détections.
- **Notation** : 10/10 si FPR ≤ 0.05, linéairement décroissant jusqu’à 0/10 si FPR ≥ 0.3.


### Tableau récapitulatif

| Critère                            | Pondération | Description                        |
| ---------------------------------- | ----------- | ---------------------------------- |
| Nombre d’individus détectés        | 25          | Écart absolu avec le ground truth  |
| Erreur de localisation (IoU moyen) | 25          | Précision des bounding boxes       |
| Précision (Precision)              | 10          | Proportion de détections correctes |
| Rappel (Recall)                    | 10          | Proportion d’abeilles détectées    |
| mAP\@0.5                           | 10          | Moyenne de la précision à IoU=0.5  |
| Temps d’inférence                  | 10          | Rapidité du traitement de l’image  |
| Taux de faux positifs (FPR)        | 10          | Proportion de détections fausses   |
| **Total**                          | **100**     | Score final sur 100                |


 Code Python : [[YOLOBenchmark.py]]