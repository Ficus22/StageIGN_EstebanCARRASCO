from ultralytics import YOLO
import os

HOME = os.getcwd()

model = YOLO("yolov10m.pt")

dataset_path = os.path.join(HOME, "GeoDanceHive-BeeDataset-3", "data.yaml")
print(dataset_path)

results = model.train(
    data=dataset_path,
    epochs=100,
    batch=32,
    plots=True,
)