import nest_asyncio
import time
import pyautogui
from pymsgbox import alert
import asyncio
import time
import os
import sys
import pytesseract
import cv2
import numpy as np
import pyautogui


class Player:

    def __init__(self):
        pyautogui.useImageNotFoundException()

    def jump(self):
        pyautogui.keyDown('space')
        pyautogui.keyUp('space')

    def boost(self, x, y):
        # pyautogui.press('shiftleft')
        self.jump()
        pyautogui.click(x + 60, y + 160)
        pyautogui.moveTo(x + 100, y)

    def identifyBoost(self, screen):
        run = "run.png"
        img_rgb = cv2.imread(run)
        assert img_rgb is not None, "file could not be read, check with os.path.exists()"
        try:
            res = cv2.matchTemplate(
                img_rgb, screen, cv2.TM_CCOEFF_NORMED)
            threshold = 0.99
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                return pt
        except:
            print("Run not found")

    def identifyCoin(self, mask, roi):
        coin = "coin.png"
        img_rgb = cv2.imread(coin)
        assert img_rgb is not None, "file could not be read, check with os.path.exists()"
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(coin, cv2.IMREAD_GRAYSCALE)
        w, h = template.shape[::-1]
        try:
            res = cv2.matchTemplate(
                img_gray, mask, cv2.TM_CCOEFF_NORMED)
            threshold = 0.5125
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(
                    roi, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), 2)
                cv2.putText(
                    roi, coin, (pt[0], pt[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                return coin
        except:
            print("Coin not found")

    def identifyBox(self, mask, roi):
        box = "box.png"
        img_rgb = cv2.imread(box)
        assert img_rgb is not None, "file could not be read, check with os.path.exists()"
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(box, cv2.IMREAD_GRAYSCALE)
        w, h = template.shape[::-1]
        try:
            res = cv2.matchTemplate(
                img_gray, mask, cv2.TM_CCOEFF_NORMED)
            threshold = 0.53
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                cv2.rectangle(
                    roi, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), 2)
                cv2.putText(
                    roi, box, (pt[0], pt[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                return box

        except:
            print("Box not found")
