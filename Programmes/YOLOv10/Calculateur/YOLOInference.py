from ultralytics import YOLO

model = YOLO('runs/detect/train/weights/best.pt', task='detect')

image_path = 'ResultFiltered10032/clahe+sharp-originalimage.jpg'
results = model(image_path)

results[0].save("ResultImage2.jpg")
results[0].save_txt("ResultImage.txt")

#df = results[0].to_df()
#print(df)

