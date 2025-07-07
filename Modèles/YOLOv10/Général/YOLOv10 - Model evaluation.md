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
Pour récupérer le fichier `.txt` des labels générés par YOLO après inférence sur une image, il existe une méthode standard intégrée dans les outils Ultralytics (YOLOv5, YOLOv8, etc.) :

**L’option `--save-txt` lors de l’inférence avec le script de détection**. Par exemple :
```bash

python detect.py --source chemin/vers/image.jpg --save-txt
```

Cette option enregistre automatiquement, pour chaque image inférée, un fichier texte au format YOLO contenant les prédictions (une ligne par objet détecté : `class_index x_center y_center width height` avec coordonnées normalisées).

**Le fichier `.txt` généré porte le même nom que l’image** (par exemple, `image1.jpg` → `image1.txt`) et se trouve dans le dossier `runs/detect/exp/labels/` (ou un chemin similaire selon la version YOLO utilisée).


## Metric faite maison

#### 1. Nombre d’individus détectés (25 points)
- **But** : Évaluer l’écart absolu entre le nombre d’abeilles détectées et le nombre réel sur l’image.
- **Notation** : 25/25 si le nombre est exact, score décroissant linéairement jusqu’à 0/25 si l’écart atteint un seuil maximal (par exemple, 50 % d’erreur).

#### 2. Erreur de localisation des bounding boxes (IoU moyen) (25 points)
- **But** : Mesurer la précision de la localisation.
- **Notation** : 25/25 si l’IoU moyen ≥ 0,85, score décroissant linéairement jusqu’à 0/25 si l’IoU ≤ 0,5.

#### 3. Précision (Precision) (10 points)
- **But** : Proportion de détections correctes parmi toutes les détections.
- **Notation** : 10/10 si précision ≥ 0,95, score décroissant linéairement jusqu’à 0/10 si précision ≤ 0,7.

#### 4. Rappel (Recall) (10 points)
- **But** : Proportion d’abeilles détectées parmi toutes les abeilles présentes.
- **Notation** : 10/10 si rappel ≥ 0,95, score décroissant linéairement jusqu’à 0/10 si rappel ≤ 0,7.

#### 5. mAP@0.5 (Mean Average Precision à IoU=0.5) (10 points)
- **But** : Mesure globale de la performance sur l’image.
- **Notation** : 10/10 si mAP@0.5 ≥ 0,95, score décroissant linéairement jusqu’à 0/10 si mAP@0.5 ≤ 0,7.

#### 6. Temps d’inférence (10 points)
- **But** : Prendre en compte la rapidité du modèle.
- **Notation** : 10/10 si le temps d’inférence est inférieur à un seuil optimal (par exemple, < 100 ms), score décroissant linéairement jusqu’à 0/10 si le temps dépasse un seuil maximal (par exemple, > 1 s).

#### 7. Mémoire utilisée lors de l’inférence (10 points)
- **But** : Évaluer l’efficacité mémoire du modèle.
- **Notation** : 10/10 si la mémoire utilisée est inférieure à un seuil optimal (par exemple, < 200 Mo), score décroissant linéairement jusqu’à 0/10 si la mémoire dépasse un seuil maximal (par exemple, > 1 Go.

## Tableau récapitulatif

| Critère                            | Pondération | Description                            |
| ---------------------------------- | ----------- | -------------------------------------- |
| Nombre d’individus détectés        | 25          | Écart absolu avec le ground truth      |
| Erreur de localisation (IoU moyen) | 25          | Précision des bounding boxes           |
| Précision (Precision)              | 10          | Proportion de détections correctes     |
| Rappel (Recall)                    | 10          | Proportion d’abeilles détectées        |
| mAP\@0.5                           | 10          | Moyenne de la précision à IoU=0.5      |
| Temps d’inférence                  | 10          | Rapidité de traitement de l’image      |
| Mémoire utilisée à l’inférence     | 10          | Efficacité mémoire lors de l’inférence |
| **Total**                          | **100**     | Score final sur 100                    |

## Programme

version 1 :
```python
import numpy as np

def load_yolo_labels(txt_path):
    labels = []
    with open(txt_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            class_id = int(parts[0])
            bbox = list(map(float, parts[1:5]))  # [x_center, y_center, width, height]
            labels.append({'class': class_id, 'bbox': bbox})
    return labels

def bbox_iou(box1, box2):
    def to_corners(box):
        x, y, w, h = box
        return [x - w/2, y - h/2, x + w/2, y + h/2]
    b1 = to_corners(box1)
    b2 = to_corners(box2)
    xi1, yi1 = max(b1[0], b2[0]), max(b1[1], b2[1])
    xi2, yi2 = min(b1[2], b2[2]), min(b1[3], b2[3])
    inter_area = max(0, xi2 - xi1) * max(0, yi2 - yi1)
    b1_area = (b1[2] - b1[0]) * (b1[3] - b1[1])
    b2_area = (b2[2] - b2[0]) * (b2[3] - b2[1])
    union_area = b1_area + b2_area - inter_area
    return inter_area / union_area if union_area > 0 else 0

def match_boxes(gt_labels, pred_labels, iou_thresh=0.5):
    matches = []
    gt_matched = set()
    pred_matched = set()
    for i, gt in enumerate(gt_labels):
        best_iou = 0
        best_j = -1
        for j, pred in enumerate(pred_labels):
            if pred['class'] == gt['class'] and j not in pred_matched:
                iou = bbox_iou(gt['bbox'], pred['bbox'])
                if iou > best_iou:
                    best_iou = iou
                    best_j = j
        if best_iou >= iou_thresh and best_j >= 0:
            matches.append((i, best_j, best_iou))
            gt_matched.add(i)
            pred_matched.add(best_j)
    return matches, gt_matched, pred_matched

def compute_metrics(gt_labels, pred_labels, inference_time_ms, memory_mb):
    n_gt = len(gt_labels)
    n_pred = len(pred_labels)
    matches, gt_matched, pred_matched = match_boxes(gt_labels, pred_labels)
    n_matched = len(matches)
    ious = [iou for _, _, iou in matches]

    # Nombre d'individus détectés (25 points)
    rel_error = abs(n_pred - n_gt) / max(1, n_gt)
    score_count = 25 * (1 - min(rel_error / 0.5, 1))  # 0 si >= 50% d'erreur

    # IoU moyen (25 points)
    iou_mean = np.mean(ious) if ious else 0
    score_iou = 25 * (iou_mean - 0.5) / 0.35 if iou_mean >= 0.5 else 0
    score_iou = min(max(score_iou, 0), 25)

    # Précision (10 points)
    precision = n_matched / n_pred if n_pred > 0 else 0
    score_precision = 10 * (precision - 0.7) / 0.25 if precision >= 0.7 else 0
    score_precision = min(max(score_precision, 0), 10)

    # Rappel (10 points)
    recall = n_matched / n_gt if n_gt > 0 else 0
    score_recall = 10 * (recall - 0.7) / 0.25 if recall >= 0.7 else 0
    score_recall = min(max(score_recall, 0), 10)

    # mAP@0.5 (10 points, approximation sur une image)
    ap = n_matched / (n_pred + n_gt - n_matched) if (n_pred + n_gt - n_matched) > 0 else 0
    score_map = 10 * (ap - 0.7) / 0.25 if ap >= 0.7 else 0
    score_map = min(max(score_map, 0), 10)

    # Temps d'inférence (10 points)
    if inference_time_ms < 100:
        score_time = 10
    elif inference_time_ms > 1000:
        score_time = 0
    else:
        score_time = 10 * (1 - (inference_time_ms - 100) / 900)

    # Mémoire utilisée (10 points)
    if memory_mb < 200:
        score_memory = 10
    elif memory_mb > 1000:
        score_memory = 0
    else:
        score_memory = 10 * (1 - (memory_mb - 200) / 800)

    # Score final
    score_total = score_count + score_iou + score_precision + score_recall + score_map + score_time + score_memory

    details = {
        'score_total': round(score_total, 2),
        'score_count': round(score_count, 2),
        'score_iou': round(score_iou, 2),
        'score_precision': round(score_precision, 2),
        'score_recall': round(score_recall, 2),
        'score_map': round(score_map, 2),
        'score_time': round(score_time, 2),
        'score_memory': round(score_memory, 2),
        'precision': round(precision, 3),
        'recall': round(recall, 3),
        'iou_mean': round(iou_mean, 3),
        'n_gt': n_gt,
        'n_pred': n_pred,
        'n_matched': n_matched,
        'inference_time_ms': inference_time_ms,
        'memory_mb': memory_mb
    }
    return details

# Exemple d'utilisation
gt_txt = 'image_gt.txt'
pred_txt = 'image_pred.txt'
# À renseigner selon ta mesure :
inference_time_ms = 120       # par exemple, 120 ms
memory_mb = 250               # par exemple, 250 Mo

gt_labels = load_yolo_labels(gt_txt)
pred_labels = load_yolo_labels(pred_txt)
score_details = compute_metrics(gt_labels, pred_labels, inference_time_ms, memory_mb)

print("Score global sur 100 :", score_details['score_total'])
print("Détail du score :", score_details)
```