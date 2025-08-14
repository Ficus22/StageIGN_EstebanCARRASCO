from ultralytics import YOLO

model = YOLO('runs/detect/train15/weights/best.pt', task='detect')

image_path = 'Truth/truthImage.jpg'

results = model.predict(image_path, show_labels=True, show_conf=True)

results[0].save("ResultImage3.jpg")
#results[0].save_txt("ResultImage3.txt")

#print(results[0])

#df = results[0].to_df()
#print(df)

