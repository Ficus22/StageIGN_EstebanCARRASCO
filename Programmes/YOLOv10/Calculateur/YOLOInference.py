from ultralytics import YOLO

model = YOLO('Calculateur/Modèles/best001.pt', task='detect')

image_path = 'Dataset/test_frames/essaim-sur-cadre.jpg'
results = model(image_path)
results[0].show()