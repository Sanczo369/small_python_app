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