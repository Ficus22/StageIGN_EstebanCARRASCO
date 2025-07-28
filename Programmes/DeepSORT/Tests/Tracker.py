import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import random

colors = {}  # track_id : (B, G, R)
def get_color(track_id):
    if track_id not in colors:
        random.seed(track_id)  # même couleur pour un même ID
        colors[track_id] = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
    return colors[track_id]



# 1. Modèles
model = YOLO('best015.pt')
tracker = DeepSort(max_age=30, n_init=3, nn_budget=100)

# 2. Vidéo source
cap = cv2.VideoCapture('Out_UP_Extrait1_15s.mp4')
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# 3. Vidéo de sortie
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('video_resultat.mp4', fourcc, fps, (width, height))

# 4. Stockage des trajectoires
trajectories = {}  # track_id: list of (x_center, y_center)

# 5. Boucle principale
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Détection avec YOLO
    results = model(frame)
    detections = []
    for det in results[0].boxes:
        x1, y1, x2, y2 = map(float, det.xyxy[0])
        confidence = float(det.conf)
        detections.append([(x1, y1, x2, y2), confidence])

    # Suivi avec Deep SORT
    tracks = tracker.update_tracks(detections, frame=frame)
    for track in tracks:
        if not track.is_confirmed():
            continue
        x1, y1, x2, y2 = map(int, track.to_tlbr())
        track_id = track.track_id
        cx, cy = int((x1 + x2) / 2), int((y1 + y2) / 2)

        # Stocke la position dans la trajectoire
        if track_id not in trajectories:
            trajectories[track_id] = []
        trajectories[track_id].append((cx, cy))

        # Couleur spécifique à l'abeille (track_id)
        color = get_color(track_id)

        # Dessin de la boîte et ID
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f"ID {track_id}", (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        # Dessin de la trajectoire
        pts = trajectories[track_id]
        for i in range(1, len(pts)):
            cv2.line(frame, pts[i-1], pts[i], color, 2)


    out.write(frame)

# Libération des ressources
cap.release()
out.release()
cv2.destroyAllWindows()
