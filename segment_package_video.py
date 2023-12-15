from ultralytics import YOLO

import cv2

model = YOLO("package_1215_n.pt")

# result = model.predict(source=""your video"",name="package",show=False,save=True)
result = model.predict(source="your video",show=True)
print(result)
