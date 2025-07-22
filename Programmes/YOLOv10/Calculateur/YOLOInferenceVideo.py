import cv2
from ultralytics import YOLO

model = YOLO('runs/detect/train15/weights/best.pt')

cap = cv2.VideoCapture('Out_UP_Extrait1_15s.mp4')

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la vidéo.")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS) or 20.0

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('bbox_only_output.mp4', fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)[0]

    # Dessiner uniquement les bounding boxes (sans labels)
    for box in results.boxes.xyxy.cpu().numpy():
        x1, y1, x2, y2 = map(int, box[:4])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    out.write(frame)

cap.release()
out.release()
