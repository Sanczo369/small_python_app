import cv2
import math
import cvzone
import threading
from ultralytics import YOLO

# Load YOLO model with custom weights
yolo_model = YOLO("Weights/best.pt")

# Define class names
class_labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

frame = None

def capture_video(video_capture):
    global frame
    while True:
        success, img = video_capture.read()
        if success:
            frame = img

# For number detection through webcam
video_capture = cv2.VideoCapture(0)

# For number detection through ip webcam
# url = 'ip_address_here/video'
# video_capture = cv2.VideoCapture(url)

# For number detection in a video
# video_path = "video_file_here"
# video_capture = cv2.VideoCapture(url)

# Start the video capture in a separate thread
capture_thread = threading.Thread(target=capture_video, args=(video_capture,))
capture_thread.daemon = True
capture_thread.start()

while True:
    # Perform object detection
    results = yolo_model(frame)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            w, h = x2 - x1, y2 - y1

            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])

            if conf > 0.3:
                cvzone.cornerRect(frame, (x1, y1, w, h), t=2)
                cvzone.putTextRect(frame, f'{class_labels[cls]} {conf}', (x1, y1 - 10), scale=0.8, thickness=1,
                                   colorR=(255, 0, 0))

    # Display the frame with detections
    cv2.imshow("Image", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cv2.waitKey(1)