import pyautogui
import time

# 매크로
# pyautogui.position()
pyautogui.moveTo(728, 104, 2)

# pyautogui.click(clicks=2, interval=2)
pyautogui.doubleClick() # 파일 열리고

time.sleep(1) # 1초 쉬고

# pyautogui.typewrite('Hello') # Hello 쓰기
pyautogui.typewrite(['enter']) # 엔터키