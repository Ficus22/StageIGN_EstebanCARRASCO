import cv2
import torch
from ultralytics import YOLO
import time
from bytetrack import BYTETracker 

# Charger modèle YOLO (exemple avec yolov8n)
model = YOLO('best015.pt')

# Initialiser ByteTrack avec paramètres par défaut, configurable
tracker = BYTETracker(
    track_thresh=0.5, 
    track_buffer=30, 
    match_thresh=0.9, 
    frame_rate=30
)

# Ouvrir la vidéo ou la caméra
cap = cv2.VideoCapture("Out_UP_Extrait1_15s.mp4")

# Prepare output video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = cap.get(cv2.CAP_PROP_FPS)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out_path = "TrackingVideo.mp4"
out = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Détection objets avec YOLO
    results = model(frame)[0]

    # Préparer les détections pour ByteTrack: format [x1, y1, x2, y2, score]
    dets = []
    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        conf = box.conf[0]
        dets.append([x1.item(), y1.item(), x2.item(), y2.item(), conf.item()])
    dets = torch.tensor(dets)

    # Mise à jour du tracker
    tracked_objects = tracker.update(dets.cpu(), frame)

    # Affichage
    for track in tracked_objects:
        x1, y1, x2, y2 = map(int, track.tlbr)
        track_id = track.track_id
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f'ID: {track_id}', (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow('YOLO + ByteTrack Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()


print("Processing complete. Process spend:", round(end-begin, 2), "s. ","The output video is saved to:", out_path)