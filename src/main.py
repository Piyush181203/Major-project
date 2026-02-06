import cv2
from vehicle_detection import VehicleDetector
from congestion_prediction import CongestionPredictor

def main(video_path):
    cap = cv2.VideoCapture(video_path)
    detector = VehicleDetector(model_path="models/yolov5/yolov5s.pt")
    predictor = CongestionPredictor()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        vehicles = detector.detect(frame)
        density = len(vehicles)
        congestion_level = predictor.predict(density)

        cv2.putText(frame, f"Density: {density}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        cv2.putText(frame, f"Congestion: {congestion_level}", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        cv2.imshow("Traffic Monitoring", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", type=str, default="data/sample_video.mp4")
    args = parser.parse_args()
    main(args.video)
