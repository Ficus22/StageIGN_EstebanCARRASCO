from ultralytics import YOLO

model = YOLO("yolov10n.pt")

result = model.track(0, save=True, show=True, conf=0.15)