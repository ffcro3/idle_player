import cv2
from tracker import *
from PIL import ImageGrab
import numpy as np
import pygetwindow as gw
from Player import *
from OCR import *
from Bonus import *
from screenCapture import setInterval, capture
import threading

# Create tracker object
tracker = EuclideanDistTracker()

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(
    history=100, varThreshold=40)

area_config = 1298
tentativa = 0
Player_1 = Player()
ocr = OCR()
bonus = Bonus()

while True:
    tentativa = tentativa + 1
    captureScreen = capture()
    frame = captureScreen[0]
    screen = captureScreen[1]

    # Extract Region of interest
    roi = frame[100:, 220:600]

    # 1. Object Detection
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 252, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # if tentativa >= 40 and tentativa <= 45:
    #     ocr.takeSS(screen, tentativa, 8, 10)

    # else:

    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > area_config:
            Player_1.Play(roi)

    boost = Player_1.identifyBoost(screen)
    if boost:
        Player_1.boost(boost[0], boost[1])

    chest_hunt = Player_1.chestHunt(screen)
    if chest_hunt:
        Player_1.click(chest_hunt[0], chest_hunt[1])

    # bonus_check = bonus.find_ui(screen, 'bonus_swipe_1.png')
    # if bonus_check != None:
    #     bonus_check_end = bonus.find_ui(screen, 'bonus_swipe_2.png')
    #     Player_1.Swipe(bonus_check, bonus_check_end)
    # else:
    #     pass

    # second_wind = ocr.find_ui(screen, 'bonus_wind.png')
    # if second_wind:
    #     Player_1.click(second_wind[0], second_wind[1])
    # else:
    #     pass

    # cv2.imshow("roi", roi)
    # cv2.imshow("Frame", frame)

    # key = cv2.waitKey(30)
    # if key == 27:
    #     break

cv2.destroyAllWindows()
