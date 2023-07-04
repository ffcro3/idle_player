import cv2
from tracker import *
from PIL import ImageGrab
import numpy as np
import pygetwindow as gw
from Player import *

# Create tracker object
tracker = EuclideanDistTracker()

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(
    history=100, varThreshold=40)

area_config = 1298
Player_1 = Player()

while True:
    chosenWindow = gw.getWindowsWithTitle('Idle Slayer')[0]
    screen = np.array(ImageGrab.grab(bbox=(
        chosenWindow.topleft[0], chosenWindow.topleft[1], chosenWindow.bottomright[0], chosenWindow.bottomright[1])))
    screen = cv2.cvtColor(src=screen, code=cv2.COLOR_BGR2RGB)
    frame = screen
    height, width, _ = frame.shape

    # Extract Region of interest
    roi = frame[100:, 220:510]

    # 1. Object Detection
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 252, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > area_config:
            coin = Player_1.identifyCoin(mask, roi)
            box = Player_1.identifyBox(mask, roi)
            if coin or box:
                Player_1.jump()

    boost = Player_1.identifyBoost(screen)
    if boost:
        Player_1.boost(boost[0], boost[1])

#     cv2.imshow("roi", roi)
#     cv2.imshow("Frame", frame)
#     cv2.imshow("Mask", mask)

#     key = cv2.waitKey(30)
#     if key == 27:
#         break

# cv2.destroyAllWindows()
