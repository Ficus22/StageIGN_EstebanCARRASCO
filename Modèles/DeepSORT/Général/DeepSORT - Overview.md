---
tags:
  - recherches
  - programme
Date: 2025-07-23
References: "[[Bibliographie.canvas|Bibliographie]]"
Objectif: Prise en main
aliases:
---
# Utilisation de Deep SORT après YOLOv10 pour le suivi des trajectoires

## Principe général
La combinaison YOLO + Deep SORT est largement adoptée pour le suivi automatique d’objets en mouvement, notamment pour des applications nécessitant la traçabilité de cibles petites et nombreuses, comme les abeilles sur les cadres de la GDH. La méthode fonctionne en deux étapes :

- **YOLO (You Only Look Once)** détecte chaque abeille sur chaque image ou frame vidéo, en produisant des boîtes englobantes identifiant la position de chaque individu à chaque instant.
- **Deep SORT (Simple Online and Realtime Tracking with a Deep Association Metric)** reçoit ces détections image après image et attribue un identifiant unique à chaque abeille, générant ainsi des trajectoires individuelles au fil du temps.


## Comment ça fonctionne en pratique
- Deep SORT prend pour entrée les détections fournies par YOLO à chaque frame.
- Il utilise simultanément les informations de mouvement (via un filtre de Kalman) et d’apparence (descripteurs visuels extraits par un réseau neuronal) pour reconnaître et suivre chaque abeille d’une image à l’autre.
    - Cela permet d’éviter la confusion d’identités lors de croisements, d’occlusions ou de recouvrements fréquents au sein du groupe.
    - Le suivi fonctionne même si une abeille disparaît temporairement (ex : devient floue ou repasse derrière une autre), grâce à la mémoire temporelle et à la carte des similarités.
- Les trajectoires ainsi obtenues sont censées être robustes, chaque trajectoire correspondant à une abeille précise et permettant l’analyse de son comportement, sa vitesse, ou ses positions par rapport aux autres.


## Code exemple (à tester)
```python
import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort

# 1. Chargez vos modèles
model = YOLO('votre_modele.pt')
tracker = DeepSort(max_age=30, n_init=3, nn_budget=100)

# 2. Configuration de la vidéo
cap = cv2.VideoCapture('votre_video.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break

    # 3. Détection YOLO
    results = model(frame)
    detections = []
    for det in results[0].boxes:
        x1, y1, x2, y2 = map(float, det.xyxy[0])
        confidence = float(det.conf)
        detections.append([(x1, y1, x2, y2), confidence])

    # 4. Tracking Deep SORT
    tracks = tracker.update_tracks(detections, frame=frame)
    for track in tracks:
        if not track.is_confirmed(): continue
        x1, y1, x2, y2 = map(int, track.to_tlbr())
        track_id = track.track_id
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, f"ID {track_id}", (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    # Affichage ou sauvegarde
    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break
cap.release()
cv2.destroyAllWindows()

```