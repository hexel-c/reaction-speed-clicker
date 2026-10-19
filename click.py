import pyautogui

isRunning = True 

while(isRunning):
    pyautogui.FAILSAFE = True
    position = pyautogui.position()
    x, y = position.x, position.y
    color = pyautogui.pixel(x,y)
    print(f"X: {x}, Y {y}, RGB: {color}")
    print(position)

    if (color == (75, 219, 106)):
        pyautogui.click()

    if (color == (43, 135, 209)):
            pyautogui.click()