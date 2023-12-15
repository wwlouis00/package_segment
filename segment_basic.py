from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2
model = YOLO("model/yolov8n-seg.pt")

result = model.predict(source='0',show=True)
# result = model.predict(source="your video or image",project="save dir",name="file name",show=True,save=True)
print(result)
