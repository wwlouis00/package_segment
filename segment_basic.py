from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2
model = YOLO("model/yolov8m-seg.pt")

result = model.predict(source='0',show=True)
# result = model.predict(source="/home/wwlouis/project/yolov8/video/frame_60488.jpg",project="result/detection/",name="package",show=True,save=True)
print(result)
