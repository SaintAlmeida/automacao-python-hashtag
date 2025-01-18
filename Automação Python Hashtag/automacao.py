import pyautogui as pa
import time

#Funções de mouse
time.sleep(3)
#pa.click(x=934, y=116)
pa.moveTo(x=934, y=116, duration =2)
pa.PAUSE = 2
pa.click(x=805, y=260, duration=2)
pa.scroll(-150)