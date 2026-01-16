import sys

import pyautogui
import time
import pyscreeze

time.sleep(1)
pyautogui.PAUSE = 0.4
work = sys.argv[1]

try:
    pyautogui.locateCenterOnScreen(r"D:\Checker\button.png", confidence=0.8, grayscale=True)
except Exception:
    pyautogui.click(pyautogui.locateCenterOnScreen(r'D:\Checker\taskbar.png', confidence=0.9, grayscale=True))

pyautogui.moveTo(65, 513)
pyautogui.scroll(1000)
pyautogui.click(55, 357)

pyautogui.moveTo(271, 574)
pyautogui.scroll(1000)
pyautogui.click(pyautogui.locateCenterOnScreen(r'D:\Checker\update.png', confidence=0.8, grayscale=True))
pyautogui.write(work)
pyautogui.press('enter')
pyautogui.click(pyautogui.locateCenterOnScreen(r'D:\Checker\close.png', confidence=0.9, grayscale=True))

