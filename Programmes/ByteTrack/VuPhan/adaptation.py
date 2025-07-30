from bytetrack.byte_track import ByteTrack
from dataclasses import dataclass

from supervision import ColorPalette, ColorLookup
from supervision import VideoInfo, VideoSink, get_video_frames_generator
from supervision import BoundingBoxAnnotator, LabelAnnotator, TraceAnnotator
from supervision import Detections


import numpy as np
from ultralytics import YOLO
import time
import json



INPUT_PATH = "UP_Extrait1_15s.mp4"
OUTPUT_PATH = "TrackingVideo.mp4"

label_mode = False
palette_name = 'hsv'

# 1: default | 2: original | 3: white | 4: black | 5: json
video_type = 1 

GPT_PALETTE = [
    "#FF0000", "#036B03", "#FFFF00", "#FF00FF", "#00FFFF",
    "#FF6600", "#66FF00", "#00FF66", "#6600FF", "#FF0066",
    "#CC0000", "#00CC00", "#CCCC00", "#CC00CC", "#00CCCC",
    "#FF3300", "#33FF00", "#00FF33", "#FF0033",
    "#990000", "#009900", "#999900", "#990099", "#009999",
    "#FF9900", "#99FF00", "#00FF99", "#9900FF", "#FF0099",
    "#FF1A1A", "#1AFF1A", "#FFFF1A", "#FF1AFF", "#1AFFFF",
    "#FF3300", "#195019", "#FFFF33", "#FF33FF", "#B0C7C7",
    "#CC3300", "#2A4122", "#00CC33", "#ACA0CF", "#CC0033",
    "#CC6600", "#66CC00", "#00CC66", "#9042DF", "#CC0066",
    "#FF0033", "#33FF00", "#FF3300", "#00FF33", "#FF00CC",
    "#00FFCC", "#CC00FF", "#FFCC00", "#CCFF00", "#00CCFF",
    "#FF0066", "#66FF00", "#FF6600", "#00FF66", "#FF3366",
    "#6F8369", "#232427", "#FF6633", "#696969", "#FF3399",
    "#99FF33", "#FF9933", "#33FF99", "#FF66CC", "#CCFF66",
    "#FFCC66", "#66FFCC", "#FF6699", "#99FF66", "#FF9966",
    "#66FF99", "#FF33CC", "#CCFF33", "#FFCC33", "#33FFCC",
    "#FF0033", "#33FF33", "#FF3300", "#00FF33", "#FF00AA",
    "#00FFAA", "#311D3B", "#FFAA00", "#AAFF00", "#00AAFF",
    "#FFAA33", "#1B3027", "#AA33FF", "#FF33AA", "#33AAFF",
    "#AAFF33", "#FF55FF", "#55FFFF", "#FFFF55", "#FF5555",
    "#55FF55", "#FF7777", "#77FF77", "#FF77FF", "#77FFFF",
    "#FFFF77", "#FF8800", "#00FF88", "#FF0088", "#88FF00",
    "#FFBB00", "#00FFBB", "#FF00BB", "#BBFF00", "#00BBFF",
    "#FFB3B3", "#B3FFB3", "#FFB3FF", "#B3FFFF", "#FFFFB3",
]



class ObjectTracking:
    def __init__(self, input_video_path, output_video_path) -> None:
        self.model = YOLO("best015.pt")
        self.model.fuse()

        # Mapping classe (abeilles)
        self.CLASS_NAMES_DICT = self.model.model.names
        self.CLASS_ID = [0]

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
        self.trace_annotator = TraceAnnotator(thickness=4, trace_length=100)


        # Replace BoxAnnotator with BoundingBoxAnnotator and LabelAnnotator
        self.bbox_annotator = BoundingBoxAnnotator(thickness=3)
        self.label_annotator = LabelAnnotator(text_thickness=1, text_scale=0.3, text_padding=5)

        self.seen_tracker_ids = 0

        # key: tracker_id, value: list of (x1, y1, x2, y2)
        self.trajectories = {}


    def to_json(self, detections):
        # Stockage des trajectoires
        bboxes = detections.xyxy
        track_ids = detections.tracker_id

        for bbox, track_id in zip(bboxes, track_ids):
            x1, y1, x2, y2 = bbox
            if track_id not in self.trajectories:
                self.trajectories[track_id] = []
            self.trajectories[track_id].append((x1, y1, x2, y2))

        json_trajectories = {str(track_id): [(int(x1), int(y1), int(x2), int(y2)) for x1, y1, x2, y2 in points] for track_id, points in self.trajectories.items()}

        with open("TrackTrajectories.json", "w") as f:
            json.dump(json_trajectories, f)
            
        return
    

    def callback(self, frame, index):
        original_frame = frame.copy()

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

       
        match video_type:
            case 1 | 'default':
                # ByteTrack bboxes and trajectories on YOLO basic out video 
                initial_frame = results.plot(conf=False, labels=False, boxes=True, masks=True, probs=False, kpt_line=False, line_width=2)
                bbox_flag = True

            case 2 | 'original':  
                # ByteTrack bboxes and trajectories on blank original upgraded video 
                initial_frame = original_frame
                bbox_flag = True
            
            case 3 | 'white':  
                # ByteTrack trajectories without bboxes on a white background
                initial_frame = np.full((self.video_info.height, self.video_info.width, 3), 255, dtype=np.uint8)
                bbox_flag = False

            case 4 | 'black':  
                # ByteTrack trajectories without bboxes on a black background
                initial_frame = np.zeros((self.video_info.height, self.video_info.width, 3), dtype=np.uint8)
                bbox_flag = False

            case 5 | 'json':  
                # ByteTrack data on a json file and default video generation
                initial_frame = frame.copy()
                self.to_json(detections)
                bbox_flag = True

        # Ajout des traces + boîtes + labels
        #Palette = ColorPalette.from_matplotlib(palette_name, 50)
        Palette = ColorPalette.from_hex(GPT_PALETTE)

        self.trace_annotator.color = self.bbox_annotator.color = self.label_annotator.color = Palette


        frame_traced = self.trace_annotator.annotate(initial_frame, detections=detections, custom_color_lookup=ColorLookup.TRACK)
        
        if bbox_flag :
            frame_boxes = self.bbox_annotator.annotate(frame_traced, detections=detections, custom_color_lookup=ColorLookup.TRACK)
        else:
            frame_boxes = frame_traced
        
        if label_mode:
            frame_annotated = self.label_annotator.annotate(frame_boxes, detections=detections, labels=labels, custom_color_lookup=ColorLookup.TRACK)
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
