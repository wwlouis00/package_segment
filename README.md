# Package Segmentation (Box and Object Detection Module)

## Requirements
- Support for boxes moving on a conveyor belt at a speed of 100 cm/s.
- Provide feedback on the relative coordinates of objects in the image.
- Support multiple boxes moving in parallel and return their relative coordinates.
- Support multiple cameras to enable multi-angle detection.

## Problem Handling
- Box congestion.
- Multiple objects in a single box.
- Boxes passing through red light.

## YOLOv8 Method
### Detection

## Roboflow Platform
- Easy access to the required training dataset.
- Online platform tools for image annotation with intelligent annotation assistance.
- Training data can be proportionally split.
- Supports random data augmentation with various transformations.
- Some open-source datasets offer online detection functionality.

### Roboflow Methods
- Random data augmentation.

## Training Software and Hardware Setup
| Hardware          | PC                 | Server              |
|:------------------:|:------------------:|:-------------------:|
| Pre-trained Model | YOLOv8n-seg.pt     | YOLOv8x-seg.pt      |
| System            | Ubuntu 20.04       | Ubuntu 20.04        |
| GPU               | Nvidia GeForce RTX 3060-TI 8G | Nvidia GeForce RTX 3060-TI 8G |
| CUDA              | 11.8               | 11.8                |
| Epoch             | 50                 | 50                  |
| Python            | 3.11.5             | 3.11.5              |
