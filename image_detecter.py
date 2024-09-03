from pyautogui import * 
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1 :
    if pyautogui.locateOnScreen('accept.png', confidence=0.38) != None :
        print("yes")
        print(pyautogui.locateOnScreen('accept.png', confidence=0.38))
        time.sleep(0.5)            
    else:
        print("no")
        time.sleep(0.5)        
