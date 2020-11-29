import pyautogui
import time

comments = ["Ryt Naa?","This is my bot","Want to spam someone?","DM Sunil Maharana","Just Kidding :P","Just a crazy Programmer ;)"]

time.sleep(5)

for i in range(500):
    pyautogui.typewrite(comments[i%6])
    pyautogui.typewrite("\n")
    time.sleep(1)
