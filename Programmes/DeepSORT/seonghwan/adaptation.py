import cv2
from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import numpy as np
import time

# Load YOLO model
model = YOLO("best015.pt")

# Initialize DeepSORT tracker
tracker = DeepSort(
    max_iou_distance=0.3,
    gating_only_position=True,          # limite les erreurs d'association dues à la taille/forme de la bbox
    max_cosine_distance=0.1,            # un seuil trop élevé rend le modèle aveugle à de petites différences
    max_age=20,                         # tolère les petites absences d’une même abeille avant de supprimer son identifiant
    n_init=10,                           # stabilise la création de nouvelles identités
    nms_max_overlap=0.8,
    nn_budget=150,                      # nombre max de pistes en mémoire (≈ nombre d’abeilles)
    embedder='mobilenet',               
    embedder_gpu=True,
    polygon=False,  
)


# Load the video file
video_path = "Out_UP_Extrait1_15s.mp4"
cap = cv2.VideoCapture(video_path)

# Prepare output video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = cap.get(cv2.CAP_PROP_FPS)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out_path = "TrackingVideo.mp4"
out = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

#Convert YOLO detections to a format compatible with DeepSORT
def yolo_to_detections(boxes):
    """
    Convert YOLO detections to DeepSORT-compatible format:
    [([x, y, w, h], confidence, class), ...] (list of tuples)
    """
    detections = []
    for box in boxes:
        cls_id = int(box.cls[0])    # YOLO class ID
        conf = float(box.conf[0])   # Confidence score
        x, y, w, h = box.xywh[0].cpu().numpy() #use CPU rather than GPU (.cuda()) bc doesn't work 

        bbox = [x, y, w, h]
        detections.append((bbox, conf, cls_id))
    return detections

#Main loop: read and process each frame
begin = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    #Detect objects with YOLO
    results = model.predict(frame)
    boxes = results[0].boxes

    #Convert YOLO detections to DeepSORT format
    dets_list = yolo_to_detections(boxes)

    #Update tracker with new detections
    tracks = tracker.update_tracks(dets_list, frame=frame) if len(dets_list) > 0 else []

    #Visualize tracking results on the frame
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        x, y, w, h = map(int, track.to_ltwh()) 
        cv2.putText(frame, 'X', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        label = f"ID: {track_id}"
        cv2.putText(frame, label, (x+30, y - 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    #Write the processed frame to the output video
    out.write(frame)
end = time.time()
#Release video capture and writer resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("Processing complete. Process spend:", round(end-begin, 2), "s. ","The output video is saved to:", out_path)