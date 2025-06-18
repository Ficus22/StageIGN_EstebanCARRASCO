import torch
from ultralytics import YOLO

# Charger le modèle YOLOv10 pré-entraîné
model = YOLO('yolov10n.pt')  # Remplacez par le chemin correct du modèle si nécessaire

# Charger l'image
image_path = 'test.jpg'

# Effectuer la détection d'objets
results = model(image_path)

# Afficher les résultats
results[0].show()
