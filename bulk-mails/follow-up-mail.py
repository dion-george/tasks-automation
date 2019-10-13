import pyautogui
import time
from random import randint
from pynput.keyboard import Key, Controller
keyboard = Controller()

count = 0
while count < 80:
    #click reply
    time.sleep(2)
    pyautogui.click(1745, 265)
    #click docs
    time.sleep(2)
    pyautogui.click(250, 20)
    #select and copy
    time.sleep(2)
    pyautogui.hotkey("ctrlleft", "a") 
    pyautogui.hotkey("ctrlleft", "c")
    #go back to mail
    time.sleep(2)
    pyautogui.click(150, 20)
    #paste
    time.sleep(2)
    pyautogui.hotkey("ctrlleft", "v")    
    #click send
    time.sleep(2)
    pyautogui.click(360, 172)
    #click on address in sent mail
    time.sleep(5)
    pyautogui.click(475, 870)
    #click on address in sent mail
    time.sleep(2)
    pyautogui.click(475, 870)
    #keyboard-up
    time.sleep(randint(70,120))
    keyboard.press(Key.up)
    count += 1
