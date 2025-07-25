from ultralytics import YOLO
from deep_sort_realtime.deepsort_tracker import DeepSort
import cv2
import numpy as np
import os

MODEL_PATH = "best015.pt"
VIDEO_PATH = "Out_UP_Extrait1_15s.mp4"
OUTPUT_DIR = "./frames_output"





class YoloDetector:
  def __init__(self, model_path, confidence):
    self.model = YOLO(model_path)
    self.classList = ["data"]
    self.confidence = confidence

  def detect(self, image):
    results = self.model.predict(image, conf=self.confidence, stream=True)
    result = next(results)
    detections = self.make_detections(result)
    return detections

  def make_detections(self, result):
    boxes = result.boxes
    detections = []
    for box in boxes:
      x1, y1, x2, y2 = box.xyxy[0]
      x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
      w, h = x2 - x1, y2 - y1
      class_number = int(box.cls[0])

      if result.names[class_number] not in self.classList:
        continue
      conf = box.conf[0]
      detections.append((([x1, y1, w, h]), class_number, conf))
    return detections
  


class Tracker:
  def __init__(self):
    self.object_tracker = DeepSort(
      max_age=5,
      n_init=2,
      nms_max_overlap=0.5,  # Adjusted for better overlap handling
      max_cosine_distance=0.8,
      nn_budget=None,
      override_track_class=None,
      embedder="mobilenet",
      half=True,
      bgr=True,
      embedder_model_name=None,
      embedder_wts=None,
      polygon=False,
      today=None
  )



  def track(self, detections, frame):
    tracks = self.object_tracker.update_tracks(detections, frame=frame)

    tracking_ids = []
    boxes = []
    for track in tracks:
      if not track.is_confirmed():
        continue
      tracking_ids.append(track.track_id)
      ltrb = track.to_ltrb()
      boxes.append(ltrb)

    return tracking_ids, boxes
  


colors = {}
trajectories = {}

def get_color(track_id):
    if track_id not in colors:
        np.random.seed(track_id)
        colors[track_id] = tuple(np.random.randint(0, 255, size=3).tolist())
    return colors[track_id]


def main():
    frame_count = 0
    max_frames = 15

    detector = YoloDetector(model_path=MODEL_PATH, confidence=0.4)
    tracker = Tracker()

    cap = cv2.VideoCapture(VIDEO_PATH)

    if not cap.isOpened():
        print("Error: Unable to open video file.")
        exit()


    while frame_count < max_frames:
        ret, frame = cap.read()
        if not ret:
            break

        # Detect objects on the resized 416x416 frame
        detections = detector.detect(frame)
        tracking_ids, boxes = tracker.track(detections, frame)



        # Draw the bounding boxes on the original frame (resize back)
        for tracking_id, bbox in zip(tracking_ids, boxes):

            color = get_color(tracking_id)

            # Draw the bounding box and tracking ID on the original frame
            cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), color, 2)
            cv2.putText(frame, f"{str(tracking_id)}", (bbox[0], bbox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        
        filename = os.path.join(OUTPUT_DIR, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(filename, frame)
        frame_count += 1
    

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()