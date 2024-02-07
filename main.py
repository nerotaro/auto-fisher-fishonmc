from pyautogui import *
import pyautogui
import time
import win32api, win32con
print("------ AUTOFISHER ------")
print("----- MADE BY NERO -----\n")

running = True

fishmenucolor = (84, 84, 252)
fishmenupos = (860, 470)

gamebordercolor = ((133, 95, 50), (138, 99, 60), (133, 95, 50), (204, 179, 56), (44,31,20))
gameborderpos = (900, 912)

colors = ((56,108,166))
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.1) 
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

def fish():
    print("fish went through")
    click()
    time.sleep(.2)
    pic = pyautogui.screenshot()
    if pic.getpixel(gameborderpos) in gamebordercolor:
        print("minigame started")
    while pic.getpixel(gameborderpos) in gamebordercolor:
        pic = pyautogui.screenshot()
        if not pic.getpixel((922, 900)) in colors:
            pyautogui.keyDown("shift")
        else:
            pyautogui.keyUp("shift")
    time.sleep(2)
    pyautogui.keyUp("shift")
    click()
while True:
    if pyautogui.screenshot().getpixel((fishmenupos)) == fishmenucolor:
        fish()