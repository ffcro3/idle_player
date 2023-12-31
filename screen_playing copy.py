import cv2
from tracker import *
from time import time
from PIL import ImageGrab
import numpy as np
import pygetwindow as gw
import pyautogui
import time
from Player import *
# Create tracker object
tracker = EuclideanDistTracker()

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(
    history=100, varThreshold=40)

area_config = 1298
Player_1 = Player(tentativa=0, jumps=0, runs=0, active=True)

while True:
    chosenWindow = gw.getWindowsWithTitle('Idle Slayer')[0]
    screen = np.array(ImageGrab.grab(bbox=(
        chosenWindow.topleft[0], chosenWindow.topleft[1], chosenWindow.bottomright[0], chosenWindow.bottomright[1])))
    screen = cv2.cvtColor(src=screen, code=cv2.COLOR_BGR2RGB)
    frame = screen
    height, width, _ = frame.shape

    # Extract Region of interest
    roi = frame[150: 400, 200: 400]

    # 1. Object Detection
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 252, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > area_config:
            x, y, w, h = cv2.boundingRect(cnt)
            detections.append([x, y, w, h])

    # 2. Object Tracking
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y - 15),
                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)
    if key == 27:
        break

cv2.destroyAllWindows()
