import cv2
from tracker import *
from PIL import ImageGrab
import numpy as np
import pygetwindow as gw
from Player import *
from OCR import *
from Bonus import *
import threading
import time

StartTime = time.time()


def capture():
    chosenWindow = gw.getWindowsWithTitle('Idle Slayer')[0]
    screen = np.array(ImageGrab.grab(bbox=(
        chosenWindow.topleft[0], chosenWindow.topleft[1], chosenWindow.bottomright[0], chosenWindow.bottomright[1])))
    screen = cv2.cvtColor(src=screen, code=cv2.COLOR_BGR2RGB)
    frame = screen
    return print([frame, screen])


class setInterval:

    def __init__(self, interval, action):
        self.interval = interval
        self.action = action
        self.stopEvent = threading.Event()
        thread = threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self):
        nextTime = time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()):
            nextTime += self.interval
            self.action()

    def cancel(self):
        self.stopEvent.set()
