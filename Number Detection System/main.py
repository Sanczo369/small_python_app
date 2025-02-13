import cv2
import math
import cvzone
import threading
from ultralytics import YOLO

# Load YOLO model with custom weights
yolo_model = YOLO("Weights/best.pt")