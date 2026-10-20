import pyautogui

isRunning = True
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

target_colors = {(75, 219, 106), (43, 135, 209)}

while isRunning:
    x, y = pyautogui.position()
    color = pyautogui.pixel(x, y)

    if color in target_colors:
        pyautogui.click()
