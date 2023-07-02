import nest_asyncio
import time
import pyautogui
from pymsgbox import alert
import asyncio
import time
import os
import sys
import cv2
import pytesseract
import logging

nest_asyncio.apply()
pyautogui.useImageNotFoundException()


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
    run = "run.png"
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

        try:
            if os.path.exists(run):
                pyautogui.locateOnScreen(
                    run, confidence=0.99, grayscale=True, region=(649, 698, 200, 200)
                )  # type: ignore
                print("clicking on run...")

                pyautogui.click(x=762, y=798)
                runs = runs + 1
                time.sleep(1)

        except KeyboardInterrupt:
            break

        except pyautogui.ImageNotFoundException:
            print("jumping for money...")
            jumps = jumps + 1
            pyautogui.mouseDown(x=964, y=783)
            time.sleep(0.02)
            pyautogui.mouseUp(x=964, y=783)
            continue

    alert(text="Total Jumps: {}. Total Boosts: {}. Total de Ações: {}".format(
        jumps, runs, tentativa), title="Game Finished!", button="OK")
    sys.exit(0)

asyncio.run(Run())
