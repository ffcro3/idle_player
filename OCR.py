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


class OCR:

    def __init__(self):
        pass

    def getCashStart(self, image):
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        old_file = os.path.join(os.path.abspath(
            ''), "images", 'stats', 'txt', 'cash_before.txt')
        stats_file = os.path.join(os.path.abspath(
            ''), "images", 'stats', 'txt', 'cash_start.txt')
        data = pytesseract.image_to_string(image)

        with open(old_file, 'w', encoding='utf-8') as fo:
            fo.close()

        with open(old_file, 'w', encoding='utf-8') as fo:
            with open(stats_file, 'r', encoding='utf-8') as f:
                for line in f:
                    fo.write(line)
                f.close()

        with open(stats_file, 'a', encoding='utf-8') as f:
            line_split = data.split("\n")
            word_split = line_split[3].split(" ")
            f.write(word_split[1])
            # f.write(data)

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

    def takeSS(self, screen, tentativa, scroll, scroll_reset):

        if tentativa == 40:
            shop = self.find_ui(screen, "shop.png")
            if shop:
                pyautogui.click(shop[0] + 60, shop[1] + 160)
                pyautogui.moveTo(shop[0] + 60, shop[1] + 100)

        if tentativa == 41:
            options = self.find_ui(screen, "options.png")
            if options:
                pyautogui.click(options[0] + 60, options[1] + 160)
                pyautogui.moveTo(options[0] + 60, options[1])

        if tentativa == 42:
            for item in range(scroll_reset):
                pyautogui.scroll(10)
            time.sleep(1.5)

            for scroll_down in range(scroll):
                pyautogui.scroll(-10)

        if tentativa == 43:
            stat_ss = pyautogui.screenshot(region=(823, 281, 1234, 764))
            # self.getCashStart(stat_ss)

        if tentativa == 44:
            upgrade = self.find_ui(screen, "upgrades.png")
            pyautogui.click(upgrade[0] + 60, upgrade[1] + 160)
            pyautogui.moveTo(upgrade[0] + 60, upgrade[1])

        if tentativa == 45:
            close_upgrade = self.find_ui(screen, "close_upgrade.png")
            pyautogui.click(close_upgrade[0] + 60, close_upgrade[1] + 160)
            pyautogui.moveTo(close_upgrade[0] + 60, close_upgrade[1])

        else:
            pass

        return
