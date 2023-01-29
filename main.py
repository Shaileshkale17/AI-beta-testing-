import pyautogui
import time
from pyautogui import click
from time import sleep

sleep(2)
cordinates = pyautogui.position()
#print(cordinates)
pyautogui.click(x=1892 , y=1067)
sleep(2)
pyautogui.click(x=1756 , y=724)
sleep(1)
pyautogui.hotkey('win','k') 
pyautogui.hotkey('tab')
pyautogui.hotkey('enter')