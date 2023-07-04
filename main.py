import cv2
from tracker import *
import imutils
import argparse
import numpy as np

# Create tracker object
tracker = EuclideanDistTracker()

cap = cv2.VideoCapture("slayer_final.mp4")
img_rgb = cv2.imread('coin.png')
assert img_rgb is not None, "file could not be read, check with os.path.exists()"
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('coin.png', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]
coin = 0

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(
    history=100, varThreshold=40)

while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape

    # Extract Region of interest
    roi = frame[120: 430, 200: 400]

    # 1. Object Detection
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    coins = []
    cv2.putText(
        roi, 'Coins: 0', (150, 0-100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 1298:
            res = cv2.matchTemplate(img_gray, mask, cv2.TM_CCOEFF_NORMED)
            threshold = 0.5124
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                coin = coin + 1
                coins_text = 'Coins: '.format(coin)
                cv2.rectangle(
                    roi, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), 2)
                cv2.putText(
                    roi, 'Coin', (pt[0], pt[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
