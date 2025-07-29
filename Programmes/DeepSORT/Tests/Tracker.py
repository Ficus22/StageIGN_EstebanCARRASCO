import cv2
from deep_sort_realtime.deepsort_tracker import DeepSort
from ultralytics import YOLO

# Charger le modèle YOLO
model = YOLO('best015.pt')

# Initialiser DeepSORT
tracker = DeepSort(max_age=30, n_init=3, nms_max_overlap=1.0, embedder='mobilenet')

cap = cv2.VideoCapture('Out_UP_Extrait1_15s.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Détection des objets avec YOLO
    detections = model(frame)[0]
    boxes = []
    confidences = []
    class_ids = []

    # On récupère les bounding boxes, scores et ids de classes
    for det in detections.boxes:
        x, y, w, h = map(int, det.xywh[0])
        conf = float(det.conf[0])
        cls = int(det.cls[0])
        boxes.append([x, y, w, h])
        confidences.append(conf)
        class_ids.append(cls)

    # Tracking avec DeepSORT
    tracks = tracker.update_tracks(boxes, confidences, class_ids, frame=frame)

    # Affichage
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        ltrb = track.to_ltrb()
        x1, y1, x2, y2 = map(int, ltrb)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
        cv2.putText(frame, f'ID: {track_id}', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    cv2.imshow('YOLO + DeepSORT tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
