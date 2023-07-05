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


class Bonus:

    def __init__(self):
        pass

    def find_ui(self, screen, ui_name):
        founded = ui_name
        img_rgb = cv2.imread(founded)

        try:
            res = cv2.matchTemplate(
                img_rgb, screen, cv2.TM_CCOEFF_NORMED)
            threshold = 0.70
            loc = np.where(res >= threshold)
            for founded_click in zip(*loc[::-1]):
                return founded_click
        except:
            print("UI not found")
