import cv2
import numpy as np
import os
from detector import YoloDetector
from tracker import Tracker

MODEL_PATH = "./models/best.pt"
VIDEO_PATH = "./rolling_video/Video_20241001164011269.avi"
OUTPUT_DIR = "DeepSORT/"

frame_count = 0
max_frames = 15


def main():
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

            # Draw the bounding box and tracking ID on the original frame
            cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 0, 255), 2)
            cv2.putText(frame, f"{str(tracking_id)}", (bbox[0], bbox[1] - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        
        filename = os.path.join(OUTPUT_DIR, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(filename, frame)
        frame_count += 1
    

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()