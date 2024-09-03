from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('+') == False :
    if pyautogui.locateOnScreen('accept.png', confidence=0.38) != None :
        print("game found !")
        #print(pyautogui.locateOnScreen('accept.png', confidence=0.38))
        x,y,z,w=pyautogui.locateOnScreen('accept.png', confidence=0.38)
        click(x+110, y+33)
        print("accepted")
        
    else:
        print("zzz")
        time.sleep(0.5)
