# import keyboard as keyboard
# from pyautogui import *
import pyautogui
import time
import keyboard
# import random
import win32api, win32con


###############################################
# pyautogui.displayMousePosition()
################################################

# X:   86 Y:  780 RGB: (253, 253, 253)
# X:  205 Y:  766 RGB: (255, 255, 255)
# X:  205 Y:  766 RGB: (255, 255, 255)
# X:  205 Y:  766 RGB: (255, 255, 255)
# X:  320 Y:  772 RGB: (255, 255, 255)
# X:  320 Y:  773 RGB: (255, 255, 255)
# X:  325 Y:  772 RGB: (255, 255, 255)
# X:  382 Y:  788 RGB: (255, 255, 255)
# X:  387 Y:  800 RGB: (255, 255, 255)
# X:  369 Y:  800 RGB: (255, 255, 255)
# X:  276 Y:  802 RGB: (255, 255, 255)
# X:  276 Y:  802 RGB: (255, 255, 255)
# X:  211 Y:  798 RGB: (255, 255, 255)
# X:  151 Y:  791 RGB: (254, 254, 254)
# X:  151 Y:  791 RGB: (254, 254, 254)
# X:   47 Y:  786 RGB: (253, 253,
##########################################
def click(x,y):
    win32api.SetCursorPos((x,y))
    # time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(52, 400)[1] == 255:
        click(52, 405)
    if pyautogui.pixel(151, 400)[1] == 255:
        click(151, 405)
    if pyautogui.pixel(275, 405)[1] == 255:
        click(275, 405)
    if pyautogui.pixel(380, 400)[1] == 255:
        click(380, 405)

    if pyautogui.pixel(52, 700)[1] == 255:
        click(52, 705)
    if pyautogui.pixel(151, 700)[1] == 255:
        click(151, 705)
    if pyautogui.pixel(275, 705)[1] == 255:
        click(275, 705)
    if pyautogui.pixel(380, 700)[1] == 255:
        click(380, 705)
