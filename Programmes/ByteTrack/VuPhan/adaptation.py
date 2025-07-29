from bytetrack.byte_track import ByteTrack
from dataclasses import dataclass

from supervision import ColorPalette
from supervision import Point, VideoInfo, VideoSink, get_video_frames_generator
from supervision import BoundingBoxAnnotator, LabelAnnotator, TraceAnnotator, LineZone, LineZoneAnnotator
from supervision import Detections

from typing import List
import numpy as np
from ultralytics import YOLO
from tqdm import tqdm
import argparse
import time


INPUT_PATH = "Out_UP_Extrait1_15s.mp4"
OUTPUT_PATH = "TrackingVideo.mp4"

label_mode = True


class ObjectTracking:
    def __init__(self, input_video_path, output_video_path) -> None:
        self.model = YOLO("best015.pt")  # Ton modèle YOLO entraîné
        self.model.fuse()

        # Mapping classe (abeilles)
        self.CLASS_NAMES_DICT = self.model.model.names
        self.CLASS_ID = [0]  # à adapter si besoin

        self.input_video_path = input_video_path
        self.output_video_path = output_video_path

        # Initialisation ByteTrack with updated parameter names
        self.byte_tracker = ByteTrack(
            track_activation_threshold=0.45,
            lost_track_buffer=300,               # 1s à 60 fps
            minimum_matching_threshold=0.8,
            frame_rate=60
        )

        # Infos vidéo & traceurs
        self.video_info = VideoInfo.from_video_path(self.input_video_path)
        self.generator = get_video_frames_generator(self.input_video_path)
        self.trace_annotator = TraceAnnotator(thickness=4, trace_length=200)


        # Replace BoxAnnotator with BoundingBoxAnnotator and LabelAnnotator
        self.bbox_annotator = BoundingBoxAnnotator(thickness=3)
        self.label_annotator = LabelAnnotator(text_thickness=1, text_scale=0.3, text_padding=5)

        self.seen_tracker_ids = 0




    def callback(self, frame, index):
        # Prédiction YOLO sur l’image
        results = self.model(frame, verbose=False)[0]
        detections = Detections.from_ultralytics(results)

        # On garde uniquement les classes ciblées
        detections = detections[np.isin(detections.class_id, self.CLASS_ID)]

        # Suivi avec ByteTrack
        detections = self.byte_tracker.update_with_detections(detections)

        # Création des labels (ex: "#4")
        labels = [
            f"#{tracker_id}"
            for tracker_id in detections.tracker_id
        ]

        # Ajout des traces + boîtes + labels
        frame_traced = self.trace_annotator.annotate(frame.copy(), detections=detections)
        frame_boxes = self.bbox_annotator.annotate(frame_traced, detections=detections)
        
        if label_mode:
            frame_annotated = self.label_annotator.annotate(frame_boxes, detections=detections, labels=labels)
        else:
            frame_annotated = frame_boxes

        for tracker_id in detections.tracker_id:
            if tracker_id > self.seen_tracker_ids:
                self.seen_tracker_ids = tracker_id
            else:
                continue

        return frame_annotated

    def process(self):
        with VideoSink(target_path=self.output_video_path, video_info=self.video_info) as sink:
            for index, frame in enumerate(self.generator):
                result_frame = self.callback(frame, index)
                sink.write_frame(result_frame)


if __name__ == "__main__":
    begin = time.time()
    obj = ObjectTracking(INPUT_PATH, OUTPUT_PATH)
    obj.process()
    end = time.time()

    print(f'Le programme a mis {round(end-begin, 2)} secondes et a détecté {obj.seen_tracker_ids} individus différents.')
