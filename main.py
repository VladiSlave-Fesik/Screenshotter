import pyautogui as pg
import time as t
import keyboard as k
import os
import datetime as dt
import pytesseract
import pyperclip as pclip
from pynput.mouse import Listener
from PIL import Image, ImageGrab

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
f = open("settings.txt", "r")
f_list = list(f.readlines())
dir = os.getcwd()
directory = str(f_list[0]).replace('Directory', '').replace('=', '').replace('\n', '').strip()
comb1 = str(f_list[1]).replace('Combination for screenshot', '').replace('=', '').replace('\n', '').strip()
comb2 = str(f_list[2]).replace('Combination for copy text region', '').replace('=', '').replace('\n', '').strip()
comb3 = str(f_list[3]).replace('Combination for screenshot region', '').replace('=', '').replace('\n', '').strip()
comb4 = str(f_list[4]).replace('Combination for change language that used for copy text', '').replace('=', '').replace(
    '\n', '').strip()
f.close()
lang = ['ukr', 'eng', 'rus']
clip_lang = lang[0]
d = dt.datetime.now()


def on_press(x, y, button, pressed):
    global first_x, first_y, second_x, second_y
    if pressed:
        print(F"First position {x, y}")
        first_x, first_y = x, y

    else:
        second_x, second_y = x, y
        print(f"Second position {x, y}")

    if not pressed:
        # Stop listener
        return False


print('Welcome to the screenshotter!')
while True:
    if comb1 != 'None':
        if k.is_pressed(comb1):
            now = str(d.day) + "_" + str(d.month) + "_" + str(d.year) + "__" + str(d.hour) + "__" + str(
                d.minute) + "__" + str(d.second)
            file_name = directory + now + '.png'
            pg.screenshot(file_name)
            print('Screnshot saved!')
            t.sleep(0.1)
    if comb2 != 'None':
        if k.is_pressed(comb2):
            t.sleep(0.5)
            with Listener(on_click=on_press) as listener:
                listener.join()
            minim_x = min(first_x, second_x)
            maxim_x = max(first_x, second_x)

            minim_y = min(first_y, second_y)
            maxim_y = max(first_y, second_y)

            im = (ImageGrab.grab(bbox=(minim_x, minim_y, maxim_x, maxim_y)))
            im.save(f'{dir}\\t.png', 'PNG')
            tes = pytesseract.image_to_string(Image.open(f'{dir}\\t.png'), lang=clip_lang)
            pclip.copy(tes)
            os.remove(f'{dir}\\t.png')
            print('Скопировано в буфер')
    if comb3 != 'None':
        if k.is_pressed(comb3):
            with Listener(on_click=on_press) as listener:
                listener.join()
            minim_x = min(first_x, second_x)
            maxim_x = max(first_x, second_x)

            minim_y = min(first_y, second_y)
            maxim_y = max(first_y, second_y)

            im = (ImageGrab.grab(bbox=(minim_x, minim_y, maxim_x, maxim_y)))
            now = str(d.day) + "_" + str(d.month) + "_" + str(d.year) + "__" + str(d.hour) + "__" + str(
                d.minute) + "__" + str(d.second)
            file_name = directory + now + '.png'
            im.save(file_name, 'PNG')
    if comb4 != 'None':
        if k.is_pressed(comb4):
            # change clip lang
            clip_lang = lang[(lang.index(clip_lang) + 1) % 3]
            print(f'Language: {clip_lang}')
            t.sleep(0.5)
