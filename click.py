import pyautogui

isRunning = True 

while(isRunning):
    pyautogui.FAILSAFE = True
    position = pyautogui.position()
    x, y = position.x, position.y
    color = pyautogui.pixel(x,y)
    print(f"X: {x}, Y {y}, RGB: {color}")
    print(position)

    if (color == (119, 216, 119)):
        pyautogui.click()

    if (color == (71, 133, 203)):
            pyautogui.click()