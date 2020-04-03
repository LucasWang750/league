#! python3


import pyautogui, sys, time, random, os
from PIL import ImageGrab, Image

print(pyautogui.size())
print(pyautogui.position())
icon = pyautogui.locateCenterOnScreen('./work2.png')
print(icon)
x, y = icon
pyautogui.moveTo(x/2,y/2)
pyautogui.mouseDown(); pyautogui.mouseUp()
time.sleep(1)

#in-game

centerX = 660
centerY = 380

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
    move(100,0)

def moveUp():
    move(0,-100)

def moveDown():
    move(0,100)


def clickShop():
    pyautogui.press('b')
    time.sleep(9)
    pyautogui.press('p')

def buyItem(name):
    clickShop()
    pyautogui.moveTo(centerX, centerY-250)
    pyautogui.mouseDown(); pyautogui.mouseUp()
    pyautogui.write(name)
    pyautogui.moveTo(centerX-400,centerY-200,1)
    pyautogui.mouseDown(); pyautogui.mouseUp()
    pyautogui.mouseDown(); pyautogui.mouseUp()

def attackMove():
    pyautogui.press('a')

def pressQ():
    pyautogui.press('q')

def pressW():
    pyautogui.press('w')

def pressE():
    pyautogui.press('e')

def pressR():
    pyautogui.press('r')

def pressD():
    pyautogui.press('d')

def pressF():
    pyautogui.press('f')

def getScreen():
    screen = ImageGrab.grab()
    os.chdir('./league')
    screen.save("screenshot" + str(int(time.time())) + ".png" , "PNG")
    

moveLeft()
moveLeft()
moveRight()
moveRight()
moveUp()
moveUp()
moveDown()
moveDown()
buyItem('Stormrazor')

def main():
    getScreen()

if __name__ == "__main__":
    main()




# pyautogui.doubleClick(x/2,y/2)

# iconLocation = pyautogui.center(icon)
# iconLocationX, iconLocationY = iconLocation
# pyautogui.moveTo(iconLocationX,iconLocationY) 
# pyautogui.click('./logo2.png')
# pyautogui.moveTo(1000,2000,2)
# pyautogui.click(x=iconLocationX,y=iconLocationY, button='left', clicks=1)
# print (currentMouseX, currentMouseY)

# print (icon)

