from ultralytics import YOLO

import cv2
model = YOLO("model/package_1030_n.pt")

result = model.predict(source='0',show=True)
print(result)
