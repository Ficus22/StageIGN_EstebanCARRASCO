from ultralytics import YOLO

model = YOLO('YOLOv10/Calculateur/Results/Result_e50_b16_t15/Best015.pt', task='detect')

image_path = 'YOLOv10/Results/ResultFiltered10032/clahe+sharp-originalimage.jpg'
results = model(image_path)

results[0].save("ResultImage3.jpg")
results[0].save_txt("ResultImage3.txt")

print(results[0])

#df = results[0].to_df()
#print(df)

