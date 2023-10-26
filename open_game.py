import subprocess
import time
import pyautogui
import pygetwindow as gw


# path = "C:\\Program Files (x86)\\AnyOTPSetup\\AnyOTP.exe"
# process = subprocess.Popen(path)

pencere_adi = "AnyOTP"  # Açılan pencerenin başlığını belirtin
uygulama_penceresi = gw.getWindowsWithTitle(pencere_adi)[0]

# Uygulamanın penceresine geçiş yapın
uygulama_penceresi.activate()

time.sleep(1)


def take_screenshot(x=1280, y=1000):
    pic = pyautogui.screenshot()
    return pic


ss = take_screenshot()
x, y = pyautogui.locateCenterOnScreen("images/1.png")
pyautogui.click(x, y)
time.sleep(0.3)
x, y = pyautogui.locateCenterOnScreen("images/0.png")
pyautogui.click(x, y)
time.sleep(0.3)
x, y = pyautogui.locateCenterOnScreen("images/2.png")
pyautogui.click(x, y)
time.sleep(0.5)
pyautogui.click(x, y)
time.sleep(0.3)
x, y = pyautogui.locateCenterOnScreen("images/9.png")
pyautogui.click(x, y)
time.sleep(0.3)
x, y = pyautogui.locateCenterOnScreen("images/3.png")
pyautogui.click(x, y)
time.sleep(0.3)

x, y = pyautogui.locateCenterOnScreen("images/confirm.png")
pyautogui.click(x, y)
time.sleep(0.3)
