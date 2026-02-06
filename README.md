import torch
import cv2

class VehicleDetector:
    def __init__(self, model_path="yolov5s.pt"):
        self.model = torch.hub.load("ultralytics/yolov5", "custom", path=model_path)

    def detect(self, frame):
        results = self.model(frame)
        detections = results.xyxy[0].cpu().numpy()
        vehicles = [d for d in detections if int(d[5]) in [2, 3, 5, 7]]  # car, bus, truck, motorcycle
        return vehicles
