import pyautogui, sys, time, random

# Print coordinates
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

def find_match():
    pyautogui.moveTo(913, 853, 2)
    click()
    time.sleep(1)
    click()
    time.sleep(1)
    click()

def accept_match():
    pyautogui.moveTo(913,710,1)
    pyautogui.click(clicks=60, interval=2)

def select_card():
    randomNumber = random.randint(0,3)
    list_of_coordinates = [609,782,957,1131]
    pyautogui.moveTo(list_of_coordinates[randomNumber],920,2)
    click()
    click()

def earn_xp():
    pyautogui.moveTo(500,890,1)
    click()
    click()
    
def surrender():
    pyautogui.moveTo(1749,830,1)
    click()
    click()
    pyautogui.moveTo(800,792,1)
    click()
    click()
    pyautogui.moveTo(877,491,1)
    click()
    click()

def click():
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()

try:
    while True:
        print("Finding new match")
        time.sleep(5)
        find_match()
        find_match()
        accept_match()
        time.sleep(90)
        startTime = time.time()
        currentTime = time.time()
        chooseTime = time.time()
        select_card()
        while ((currentTime - startTime) < 720):
            # print((currentTime-startTime))
            if((currentTime - chooseTime) > 50):
                select_card()
                earn_xp()
                earn_xp()
                chooseTime = time.time()
            currentTime = time.time()
        print("SURRENDER NOW")
        surrender()
except KeyboardInterrupt:
    print('\n')
surrender()