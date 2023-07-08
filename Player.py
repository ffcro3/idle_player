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
        # self.jump()
        pyautogui.click(x + 60, y + 160)
        pyautogui.moveTo(x + 100, y)

    def identifyBoost(self, screen):
        run = "run.png"
        img_rgb = cv2.imread(run)
        assert img_rgb is not None, "file could not be read, check with os.path.exists()"
        try:
            res = cv2.matchTemplate(
                img_rgb, screen, cv2.TM_CCOEFF_NORMED)
            threshold = 0.95
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                return pt
        except:
            print("Boost not found")

    def identifyOrb(self, roi):
        orb = "bonus_orb.png"
        img_rgb = cv2.imread(orb)
        assert img_rgb is not None, "file could not be read, check with os.path.exists()"
        try:
            res = cv2.matchTemplate(
                img_rgb, roi, cv2.TM_CCOEFF_NORMED)
            threshold = 0.5025
            loc = np.where(res >= threshold)
            for pt in zip(*loc[::-1]):
                return orb
        except:
            print("Orb not found")

    def identifyCoin(self, roi):
        coins = ['coin.png', 'coin_side.png', 'coin_45.png']
        for coin in coins:
            img_rgb = cv2.imread(coin)
            assert img_rgb is not None, "file could not be read, check with os.path.exists()"
            try:
                res = cv2.matchTemplate(
                    img_rgb, roi, cv2.TM_CCOEFF_NORMED)
                threshold = 0.58
                loc = np.where(res >= threshold)
                for pt in zip(*loc[::-1]):
                    return coin
            except:
                print("Coin not found")

    def identifyBox(self, roi):
        boxes = ['box.png', 'box_2.png', 'box_3.png']
        for box in boxes:
            img_rgb = cv2.imread(box)
            assert img_rgb is not None, "file could not be read, check with os.path.exists()"
            try:
                res = cv2.matchTemplate(
                    img_rgb, roi, cv2.TM_CCOEFF_NORMED)
                threshold = 0.57
                loc = np.where(res >= threshold)
                for pt in zip(*loc[::-1]):
                    return box

            except:
                print("Box not found")

    def identifyEnemy(self, roi):
        enemies = ['bad_wasp.png', 'wasp_bee.png']
        for enemy in enemies:
            img_rgb = cv2.imread(enemy)
            assert img_rgb is not None, "file could not be read, check with os.path.exists()"
            try:
                res = cv2.matchTemplate(
                    img_rgb, roi, cv2.TM_CCOEFF_NORMED)
                threshold = 0.67
                loc = np.where(res >= threshold)
                for pt in zip(*loc[::-1]):
                    return enemy

            except:
                print("Box not found")

    def chestHunt(self, roi):
        chests = ['chest_hunt.png']
        for chest in chests:
            img_rgb = cv2.imread(chest)
            assert img_rgb is not None, "file could not be read, check with os.path.exists()"
            try:
                res = cv2.matchTemplate(
                    img_rgb, roi, cv2.TM_CCOEFF_NORMED)
                threshold = 0.80
                loc = np.where(res >= threshold)
                for pt in zip(*loc[::-1]):
                    return pt

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

    def Play(self, roi):
        coin = self.identifyCoin(roi)
        box = self.identifyBox(roi)
        enemy = self.identifyEnemy(roi)
        if coin or box or enemy:
            self.jump()
