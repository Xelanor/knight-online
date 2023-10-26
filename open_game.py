import os
import subprocess
import time
import pyautogui
import pygetwindow as gw

from interception import *
from win32api import GetSystemMetrics

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
    "*": 0x37,
}

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

keyboard = 1
for i in range(MAX_DEVICES):
    if interception.is_keyboard(i):
        keyboard = i
        break

# no mouse we quit
# if keyboard == 0:
#     print("No keyboard found")
#     exit(0)


# get screen size
screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)

context = interception()


def locateCenterOfImageAndClick(image, confidence=None, sleep=None):
    x, y = pyautogui.locateCenterOnScreen(image, confidence=0.90)
    pyautogui.click(x, y)
    time.sleep(sleep)
    return True


def take_screenshot(x=1280, y=1000):
    pic = pyautogui.screenshot()
    return pic


def copyFromAnyOtp():
    try:
        pencere_adi = "AnyOTP"  # Açılan pencerenin başlığını belirtin
        uygulama_penceresi = gw.getWindowsWithTitle(pencere_adi)[0]

        # Uygulamanın penceresine geçiş yapın
        uygulama_penceresi.activate()
        time.sleep(1)
    except:
        path = "C:\\Program Files (x86)\\AnyOTPSetup\\AnyOTP.exe"
        process = subprocess.Popen(path)
        time.sleep(3)

    locateCenterOfImageAndClick("images/1_lap.png", confidence=0.90, sleep=0.3)
    locateCenterOfImageAndClick("images/0_lap.png", confidence=0.90, sleep=0.3)
    locateCenterOfImageAndClick("images/2_lap.png", confidence=0.90, sleep=0.5)
    pyautogui.click()
    time.sleep(0.3)
    locateCenterOfImageAndClick("images/9_lap.png", confidence=0.90, sleep=0.3)
    locateCenterOfImageAndClick("images/3_lap.png", confidence=0.90, sleep=0.5)
    locateCenterOfImageAndClick("images/confirm_lap.png", confidence=0.85, sleep=0.5)
    locateCenterOfImageAndClick("images/copy_code.png", confidence=0.85, sleep=0.5)


time.sleep(2)


def write_word(word):
    for letter in word:
        interception_press = key_stroke(
            keycodes[letter], interception_key_state.INTERCEPTION_KEY_DOWN.value, 0
        )
        context.send(keyboard, interception_press)
        time.sleep(0.2)
        interception_press.state = interception_key_state.INTERCEPTION_KEY_UP.value
        context.send(keyboard, interception_press)


def write_code(code):
    interception_press = key_stroke(
        code, interception_key_state.INTERCEPTION_KEY_DOWN.value, 0
    )
    context.send(keyboard, interception_press)
    time.sleep(0.5)
    interception_press.state = interception_key_state.INTERCEPTION_KEY_UP.value
    context.send(keyboard, interception_press)


def write_password():
    interception_press = key_stroke(
        0x2A, interception_key_state.INTERCEPTION_KEY_DOWN.value, 0
    )
    context.send(keyboard, interception_press)
    write_word("B")
    time.sleep(0.2)
    interception_press.state = interception_key_state.INTERCEPTION_KEY_UP.value
    context.send(keyboard, interception_press)
    write_word("ERKE123*")


def paste():
    interception_press = key_stroke(
        0x1D, interception_key_state.INTERCEPTION_KEY_DOWN.value, 0
    )
    context.send(keyboard, interception_press)
    write_word("V")
    time.sleep(0.5)
    interception_press.state = interception_key_state.INTERCEPTION_KEY_UP.value
    context.send(keyboard, interception_press)
    time.sleep(1)
    write_code(0x1C)  # ENTER


write_word("XELANOR100")
time.sleep(1)
write_code(0x0F)  # TAB
write_password()
write_code(0x1C)  # ENTER
copyFromAnyOtp()
pencere_adi = "Knight OnLine Client"  # Açılan pencerenin başlığını belirtin
uygulama_penceresi = gw.getWindowsWithTitle(pencere_adi)[0]

# Uygulamanın penceresine geçiş yapın
uygulama_penceresi.activate()
time.sleep(1)
paste()

# os.startfile("C:\\NTTGame\\KnightOnlineEn\\Launcher.exe")
# time.sleep(3)
# x, y = pyautogui.locateCenterOnScreen("images/start_btn.png", confidence=0.90)
# time.sleep(1)

# mstroke = mouse_stroke(
#     interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN.value,
#     interception_mouse_flag.INTERCEPTION_MOUSE_MOVE_ABSOLUTE.value,
#     0,
#     int((0xFFFF * x) / screen_width),
#     int((0xFFFF * y) / screen_height),
#     0,
# )
# context.send(mouse, mstroke)
# time.sleep(2)
# mstroke.state = interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_UP.value
# context.send(mouse, mstroke)
