import multiprocessing
from multiprocessing import Pool
import time
import keyboard
import pyautogui
import numpy
import win32api, win32con
import time
from datetime import datetime
import logging
import pydirectinput
from time import sleep

import threading
from interception import *
from win32api import GetSystemMetrics


def take_screenshot(x=1280, y=1000):
    pic = pyautogui.screenshot(region=(0, 0, x, y))
    # pic.save('images/ss-repair-3.png')
    return pic


keycodes = {
    "F1": 0x3B,
    "F2": 0x3C,
    "F3": 0x3D,
    "F4": 0x3E,
    "F5": 0x3F,
    "F6": 0x40,
    "F7": 0x41,
    "F8": 0x42,
    "F9": 0x43,
    "F10": 0x44,
    "F11": 0x57,
    "F12": 0x58,
    "F13": 0x64,
    "F14": 0x65,
    "F15": 0x66,
    "0": 0x0B,
    "1": 0x02,
    "2": 0x03,
    "3": 0x04,
    "4": 0x05,
    "5": 0x06,
    "6": 0x07,
    "7": 0x08,
    "8": 0x09,
    "9": 0x0A,
    "A": 0x1E,
    "B": 0x30,
    "C": 0x2E,
    "D": 0x20,
    "E": 0x12,
    "F": 0x21,
    "G": 0x22,
    "H": 0x23,
    "I": 0x17,
    "J": 0x24,
    "K": 0x25,
    "L": 0x26,
    "M": 0x32,
    "N": 0x31,
    "O": 0x18,
    "P": 0x19,
    "Q": 0x10,
    "R": 0x13,
    "S": 0x1F,
    "T": 0x14,
    "U": 0x16,
    "V": 0x2F,
    "W": 0x11,
    "X": 0x2D,
    "Y": 0x15,
    "Z": 0x2C,
}

# get screen size
screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

context = interception()

# loop through all devices and check if they correspond to a mouse
mouse = 0
for i in range(MAX_DEVICES):
    if interception.is_mouse(i):
        mouse = i
        break

# no mouse we quit
if mouse == 0:
    print("No mouse found")
    exit(0)


### GENIE BAŞLATMA ###
time.sleep(1)
# ss = take_screenshot()
# genie_start_btn_x, genie_start_btn_y = pyautogui.locateCenterOnScreen("images/genie_start_btn.png")
# print(genie_start_btn_x, genie_start_btn_y)

mstroke = mouse_stroke(
    interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN.value,
    interception_mouse_flag.INTERCEPTION_MOUSE_MOVE_ABSOLUTE.value,
    0,
    int((0xFFFF * 1000) / screen_width),
    int((0xFFFF * 400) / screen_height),
    0,
)
context.send(mouse, mstroke)
time.sleep(3)
mstroke.state = interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_UP.value
context.send(mouse, mstroke)
