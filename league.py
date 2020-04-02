#! python3


import pyautogui, sys, time, random, os, PIL
print(pyautogui.size())
print(pyautogui.position())
icon = pyautogui.locateCenterOnScreen('./work2.png')
print(icon)
x, y = icon
pyautogui.moveTo(x/2,y/2)
pyautogui.mouseDown(); pyautogui.mouseUp()
time.sleep(1)

#in-game

centerX = 720
centerY = 450


print('Press Ctrl-C to quit.')
def screenGrab():
    box = ()
    im = PIL.ImageGrab.grab()
    im.save(os.getcwd() + str(int(time.time())) +
'.png', 'PNG')

def move(x,y):
    pyautogui.moveTo(centerX+x,centerY+y)
    pyautogui.press('t')

def moveLeft():
    move(-100,0)

def moveRight():
    move(50,0)
def moveUp():
    move(0,-100)
def moveDown():
    move(0,50)

def moveRandom():
    timeout = time.time() + random.randint(1,10)
    num = random.randint(1,4)
    if num == 1:
        while True:
            if time.time() > timeout:
                break
            moveLeft()
    elif num == 2:
        while True:
            if time.time() > timeout:
                break
            moveRight()
    elif num == 3:
        while True:
            if time.time() > timeout:
                break
            moveUp()
    else:
        while True:
            if time.time() > timeout:
                break
            moveDown()
        
screenGrab()

try:
    while True:
        moveRandom()
except KeyboardInterrupt:
    print('\n')





# pyautogui.doubleClick(x/2,y/2)

# iconLocation = pyautogui.center(icon)
# iconLocationX, iconLocationY = iconLocation
# pyautogui.moveTo(iconLocationX,iconLocationY) 
# pyautogui.click('./logo2.png')
# pyautogui.moveTo(1000,2000,2)
# pyautogui.click(x=iconLocationX,y=iconLocationY, button='left', clicks=1)
# print (currentMouseX, currentMouseY)

# print (icon)

