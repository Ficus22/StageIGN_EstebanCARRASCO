from roboflow import Roboflow

rf = Roboflow(api_key="0y44LYnl73DnveDEYurR")

project = rf.workspace("geodancehive").project("geodancehive-beedataset")
version = project.version(3)
dataset = version.download("yolov8") 