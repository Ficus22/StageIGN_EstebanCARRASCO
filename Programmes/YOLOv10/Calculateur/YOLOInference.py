import torch
from torch.serialization import add_safe_globals
from ultralytics.nn.tasks import DetectionModel
from torch.nn.modules.container import Sequential
from ultralytics.nn.modules.conv import Conv  # <-- import de la classe Conv

# Ajouter toutes les classes nécessaires
add_safe_globals([DetectionModel, Sequential, Conv])

from ultralytics import YOLO

model = YOLO('Calculateur/Modèles/best001.pt', task='detect')

image_path = 'Dataset/test_frames/essaim-sur-cadre.jpg'
results = model(image_path)
results[0].show()