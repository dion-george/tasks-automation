import pyautogui
import time
from random import randint
from pynput.keyboard import Key, Controller
keyboard = Controller()

count = 0
while count < 70:
    #time.sleep(2)  
    pyautogui.click(630, 1076) 
    # Press and release space
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(1) 
    pyautogui.hotkey("ctrlleft", "c") 
    pyautogui.click(180, 20)
    # new mail
    time.sleep(1)
    pyautogui.click(180, 120) 
    # 'To' email address
    time.sleep(2)
    pyautogui.click(380, 295)
    #Paste address
    pyautogui.hotkey("ctrlleft", "v") 
    #To subject position
    time.sleep(2)
    pyautogui.click(380, 395)
    # Print Subject
    time.sleep(2)
    pyautogui.typewrite("English Grammar App Buyout Opportunity") 
    # Go to Docs
    pyautogui.click(280, 20)
    time.sleep(2)
    pyautogui.click(500, 420)
    pyautogui.hotkey("ctrlleft", "a") 
    pyautogui.hotkey("ctrlleft", "c")
    time.sleep(2)
    # Go back to mail
    pyautogui.click(180, 20)
    time.sleep(2)
    #Clicks on the body of the mail
    pyautogui.click(500, 500)
    time.sleep(2)
    pyautogui.hotkey("ctrlleft", "v")
    time.sleep(3)
    # Send the mail!
    pyautogui.click(360, 172)
    # Go to Sheets again.
    time.sleep(randint(40,65))
    pyautogui.click(50, 20) 
    # Open another application
    time.sleep(3)
    pyautogui.click(975, 1076) 
    count += 1
