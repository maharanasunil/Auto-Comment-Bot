import pyautogui
import time

comments = ["Hey","This is my bot","Spamming......","This is Fun","Try this! ","Just a crazy Programmer"]

time.sleep(5)

for i in range(500):
    pyautogui.typewrite(comments[i%6])
    pyautogui.typewrite("\n")
    time.sleep(1)
