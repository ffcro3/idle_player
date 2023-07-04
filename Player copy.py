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


nest_asyncio.apply()
pyautogui.useImageNotFoundException()


async def draw_area(x, y):
    start_point = (x, y)
    end_point = (50, 50)
    color = (255, 0, 0)
    thickness = 2
    cv2.rectangle(start_point, end_point, color, thickness)
    time.sleep(0.1)
    cv2.destroyAllWindows()


async def getCash(round, cash):
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    cash_status = os.path.join(os.path.abspath(
        ''), "images", 'stats', 'txt', 'current_cash.txt')
    stats_im = os.path.join(os.path.abspath(
        ''), "images", 'stats', 'images', 'cash', 'cash_{}.png'.format(round))
    current_cash = pyautogui.screenshot(region=(1185, 216, 100, 40))
    # current_cash.save(stats_im)
    value_cash = pytesseract.image_to_string(current_cash)
    with open(cash_status, 'a', encoding='utf-8') as f:
        if round == 1:
            cash[0] = value_cash
            f.write('Current Cash: {}\n'.format(cash))
            print(cash)
        else:
            cash[1] = value_cash
            f.write('Current Cash: {}\n'.format(cash))
            print(cash)


async def getSouls(round, soul):
    pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    souls_status = os.path.join(os.path.abspath(
        ''), "images", 'stats', 'txt', 'current_souls.txt')
    stats_im = os.path.join(os.path.abspath(
        ''), "images", 'stats', 'images', 'soul', 'souls_{}.png'.format(round))
    current_souls = pyautogui.screenshot(region=(1765, 219, 70, 33))
    # current_souls.save(stats_im)
    value_soul = pytesseract.image_to_string(current_souls, )
    with open(souls_status, 'a', encoding='utf-8') as f:  # type: ignore
        if round == 1:
            soul[0] = value_soul
            f.write('Current Souls: {}\n'.format(soul))
            print(soul)
        else:
            soul[1] = value_soul
            f.write('Current Souls: {}\n'.format(soul))
            print(soul)


async def Run():
    # NOME DO ARQUIVO
    collectables = ["run.png", "coin.png",
                    "box.png", "mushroom.png", "wasp_bee.png"]
    x = True
    tentativa = 0
    jumps = 0
    runs = 0
    cash_values = [0, 0]
    souls_values = [0, 0]

    while x == True:
        tentativa = tentativa + 1
        print('Tentativa: ', tentativa)
        # await getCash(tentativa, cash_values)
        # await getSouls(tentativa, souls_values)

        for item in collectables:

            try:

                if item == "run.png":

                    finder = pyautogui.locateOnScreen(
                        item, confidence=0.99, grayscale=True, region=(648, 152, 1280, 720)
                    )  # type: ignore

                    if finder.width != 0:
                        # await draw_area(finder.width, finder.height)
                        print('BOOST!')
                        pyautogui.click(x=762, y=798)
                        pyautogui.press('space')
                        pyautogui.moveTo(x=1175, y=798)
                        jumps = jumps + 1
                        runs = runs + 1

                if item == "box.png":
                    finder = pyautogui.locateOnScreen(
                        item, confidence=0.5, grayscale=True, region=(649, 152, 1280, 720)
                    )  # type: ignore

                    if finder.width != 0:
                        print('BOX!')
                        # await draw_area(finder.width, finder.height)
                        time.sleep(0.05)
                        pyautogui.press('space')
                        runs = runs + 1
                        jumps = jumps + 1

                if item == "coin.png":
                    finder = pyautogui.locateOnScreen(
                        item, confidence=0.5, grayscale=True, region=(649, 152, 1280, 720)
                    )  # type: ignore

                    if finder.width != 0:
                        print('COIN!')
                        # await draw_area(finder.width, finder.height)
                        time.sleep(0.2)
                        pyautogui.press('space')
                        runs = runs + 1
                        jumps = jumps + 1

                if item == "mushroom.png":

                    finder = pyautogui.locateOnScreen(
                        item, confidence=0.6, grayscale=True, region=(648, 152, 1280, 720)
                    )  # type: ignore

                    if finder.width != 0:
                        print("MUSHROOM!")
                        # await draw_area(finder.width, finder.height)
                        time.sleep(2)

                if item == "wasp_bee.png":

                    finder = pyautogui.locateOnScreen(
                        item, confidence=0.5, grayscale=True, region=(648, 152, 1280, 720)
                    )  # type: ignore

                    if finder.width != 0:
                        print('WASP/BEE!')
                        # await draw_area(finder.width, finder.height)
                        time.sleep(0.3)
                        pyautogui.press('space')
                        runs = runs + 1
                        jumps = jumps + 1

                else:
                    raise pyautogui.ImageNotFoundException()

            except KeyboardInterrupt:
                break

            except pyautogui.ImageNotFoundException:
                continue

    alert(text="Total Jumps: {}. Total Boosts: {}. Total de Ações: {}".format(
        jumps, runs, tentativa), title="Game Finished!", button="OK")
    sys.exit(0)

asyncio.run(Run())
