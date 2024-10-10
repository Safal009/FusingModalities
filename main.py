
import ultralytics
from ultralytics import YOLO

#Load  a model
model = YOLO("yolov8n.yaml")

#Use the model
results = model.train(data="config.yaml", epochs=25) #train the model
