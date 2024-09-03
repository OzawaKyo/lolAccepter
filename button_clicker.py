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

while 1 :
    if pyautogui.locateOnScreen('button.png', confidence=0.38) != None :
        print("yes")
        
        #print(pyautogui.locateOnScreen('button.png', confidence=0.38))
        x,y,z,w=pyautogui.locateOnScreen('button.png', confidence=0.38)
        click(x+77, y+95)
        time.sleep(20)
    else:
        print("no")
        time.sleep(0.5)
