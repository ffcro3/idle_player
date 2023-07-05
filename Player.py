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

    def click(self, x, y):
        pyautogui.click(x + 20, y + 160)

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
            print("Boost not found")

    def identifyOrb(self, mask):
        orb = "bonus_orb.png"
        img_rgb = cv2.imread(orb)
        assert img_rgb is not None, "file could not be read, check with os.path.exists()"
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(orb, cv2.IMREAD_GRAYSCALE)
        w, h = template.shape[::-1]
        try:
            res = cv2.matchTemplate(
                img_gray, mask, cv2.TM_CCOEFF_NORMED)
            threshold = 0.54225
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                return orb
        except:
            print("Orb not found")

    def identifyCoin(self, mask):
        coin = "coin.png"
        img_rgb = cv2.imread(coin)
        assert img_rgb is not None, "file could not be read, check with os.path.exists()"
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(coin, cv2.IMREAD_GRAYSCALE)
        w, h = template.shape[::-1]
        try:
            res = cv2.matchTemplate(
                img_gray, mask, cv2.TM_CCOEFF_NORMED)
            threshold = 0.54225
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                return coin
        except:
            print("Coin not found")

    def identifyBox(self, mask):
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
                return box

        except:
            print("Box not found")

    def Swipe(self, start, stop):
        pyautogui.mouseDown(start[0] + 10, start[1] + 160)
        pyautogui.moveTo(stop[0] + 10, start[1] + 160)
        pyautogui.mouseUp(stop[0] + 10, start[1] + 160)

    def SwipeInverse(self, start, stop):
        pass

    def IdentifyOrientationBonus(self):
        pass
