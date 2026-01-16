import pyautogui
import time
import pyscreeze

time.sleep(1)
pyautogui.PAUSE = 0.4

def sendReport():
    pyautogui.moveTo(65, 513)
    pyautogui.scroll(1000)
    pyautogui.click(pyautogui.locateCenterOnScreen(r"D:\Checker\button.png", confidence=0.8, grayscale=True))
    pyautogui.click(pyautogui.locateCenterOnScreen(r"D:\Checker\dm.png", confidence=0.8, grayscale=True))
    pyautogui.press('esc')
    pyautogui.write("[AUTOMATED SYSTEM] Please tell this user to get back to work!")
    pyautogui.press('enter')
    pyautogui.click(pyautogui.locateCenterOnScreen(r'D:\Checker\close.png', confidence=0.9, grayscale=True))

try:
    sendReport()
except Exception:
    pyautogui.click(pyautogui.locateCenterOnScreen(r'D:\Checker\taskbar.png', confidence=0.9, grayscale=True))
    sendReport()
