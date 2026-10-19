import pyautogui

isRunning = True 
pyautogui.PAUSE = 0   
pyautogui.FAILSAFE = True

target_colors = {(119, 216, 119), (71, 133, 203)}

while(isRunning):
    position = pyautogui.position()
    x, y = position.x, position.y
    color = pyautogui.pixel(x,y)

    if (color in target_colors):
        pyautogui.click()


    
