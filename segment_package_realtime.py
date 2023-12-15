from ultralytics import YOLO

import cv2
model = YOLO("model/package_1030_n.pt")

result = model.predict(source='0',show=True)
# result = model.predict(source="/home/wwlouis/project/yolov8/video/frame_60488.jpg",project="result/detection/",name="package",show=True,save=True)
print(result)
