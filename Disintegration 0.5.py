from ctypes import windll
from random import choices
from time import sleep
from pyautogui import *


# Функция для проверки раскладки клавиатуры
def check_layout():
    is_english_layout = (windll.LoadLibrary("user32.dll").GetKeyboardLayout(0) & 0xFFFF) == 0x0409
    if not is_english_layout:
        windll.user32.keybd_event(0xA0, 0, 0, 0)  # Нажатие left shift
        windll.user32.keybd_event(0xA4, 0, 0, 0)  # Нажатие left alt
        windll.user32.keybd_event(0xA4, 0, 2, 0)  # Отпускание left alt
        windll.user32.keybd_event(0xA0, 0, 2, 0)  # Отпускание left shift
        raise SystemExit("Пожалуйста, перед запуском включите английскую раскладку. Или просто перезапустите.")


# Функция для перемещения курсора
def move_to(x, y, duration=1):
    moveTo(x, y, duration=duration)


# Функция для поиска и клика по изображению
def locate_and_click(image_path, search_time=2.1):
    x, y = locateCenterOnScreen(image_path, minSearchTime=search_time)
    moveTo(x, y, duration=1)
    click()


# Функция для ввода текста с заданным интервалом
def type_with_interval(text, interval=0.4):
    for char in text:
        typewrite(char)
        sleep(interval)


# Проверка раскладки перед выполнением кода
check_layout()

# Предварительная настройка PyAutoGUI
PAUSE = 0.1
FAILSAFE = True

# Подвигаем мышью
for i in range(7, 0, -1):
    print(f"Осталось {i} секунд")
    sleep(1)
move_to(100, 100, duration=2)
move_to(200, 200)
move_to(1200, 500)

# Клик по кнопке "Пуск"
locate_and_click('start_button.png')
sleep(1)

# Ввод "PyCharm" посимвольно
type_with_interval("PyCharm", interval=1)

# Нажатие Enter
press('enter')

# Задержка перед началом создания нового файла, "PyCharm" загружается.
sleep(5)
move_to(700, 500, duration=1)
locate_and_click('PyCharm_menu_button.png')
sleep(1)

# Зажимаем Alt + Insert для создания нового файла
hotkey('alt', 'insert')
sleep(1)

# Вводим "python fi" посимвольно
type_with_interval("python fi")
press('enter')
sleep(2)

# Генерация случайной последовательности из 5 цифр и формирование имени файла
random_digits = ''.join(choices('0123456789', k=5))
file_name = f'disintegration{random_digits}'

# Ввод имени файла посимвольно
type_with_interval(file_name, interval=1)
press('enter')
sleep(1)

# Переходим в поле ввода кода
move_to(1200, 300, duration=1)
click()

# Перепечатываем весь код в новый файл, Disintegrate.py должен быть в той же папке
type_with_interval(open('Disintegrate.py', 'r').read(), interval=0.01)

# Удаление лишних строк, если это необходимо
press('delete', presses=7)
sleep(6)

# Запуск кода
hotkey('ctrl', 'shift', 'f10')
sleep(5)
