from time import sleep
import pyautogui
import random


sleep(5)
pyautogui.moveTo(100, 100, duration=2)
pyautogui.moveTo(200, 200, duration=1)
pyautogui.moveTo(1200, 500, duration=1)

start_button_x, start_button_y = pyautogui.locateCenterOnScreen('start_button.png', minSearchTime=2.1)
pyautogui.moveTo(start_button_x, start_button_y, duration=2)
sleep(1)
pyautogui.click()
sleep(1)

pyautogui.write("PyCharm", interval=0.4)
sleep(1)
pyautogui.press('enter')

sleep(5)
pyautogui.moveTo(700, 500, duration=1)
start_button_x, start_button_y = pyautogui.locateCenterOnScreen('PyCharm_menu_button.png', minSearchTime=2.1)
pyautogui.moveTo(start_button_x, start_button_y, duration=1)
sleep(1)
pyautogui.click()
sleep(2)

pyautogui.hotkey('alt', 'insert')
sleep(1)
pyautogui.write("python fi", interval=0.4)
pyautogui.press('enter')
sleep(2)

random_digits = ''.join(random.choices('0123456789', k=5))
file_name = 'disintegration{}'.format(random_digits)
print(file_name)
pyautogui.typewrite(file_name, interval=0.4)
sleep(1)
pyautogui.press('enter')

sleep(1)
pyautogui.moveTo(1200, 300, duration=1)
pyautogui.click()
sleep(1)
pyautogui.typewrite(open('Disintegrate.py', 'r').read(), interval=0.01)
pyautogui.press('delete', presses=7)
sleep(2)
pyautogui.hotkey('ctrl', 'shift', 'f10')
sleep(5)
