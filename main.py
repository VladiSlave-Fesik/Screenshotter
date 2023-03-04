try:
    import pyautogui as pg
    import time as t
    import keyboard as k
    import os
    import datetime as dt
    import pytesseract
    import pyperclip as pclip
    from pynput.mouse import Listener
    from PIL import Image, ImageGrab
    from colour import Color
    import colorit
    from PIL import ImageColor
    import time
    # import pickle
    # from PIL import Image

except ImportError as error:
    print('Import error.')
    print(error)
    input()


dir_ = os.getcwd()

# Read settings file
try:
    with open("settings.txt", "r") as f:
        f_list = f.readlines()
except FileNotFoundError:
    print("Error: settings file not found.")
    exit()

# Extract settings from file
directory = f_list[0].split('=')[1].strip()

if directory.lower() == 'none':
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
else:
    pytesseract.pytesseract.tesseract_cmd = directory

comb1 = f_list[1].split('=')[1].strip()
comb2 = f_list[2].split('=')[1].strip()
comb3 = f_list[3].split('=')[1].strip()
comb4 = f_list[4].split('=')[1].strip()

use_color = f_list[5].split('=')[1].strip()
if use_color.lower() == 'true':
    from gradient import rainbow_text
    rainbow_text('Welcome to the ScreenShotter!', 15)
else:
    print('Welcome to the ScreenShotter!')

# Print extracted settings
# print(f"Directory: {directory}")
# print(f"Combination for screenshot: {comb1}")
# print(f"Combination for copy text region: {comb2}")
# print(f"Combination for screenshot region: {comb3}")
# print(f"Combination for change language that used for copy text: {comb4}")

lang = ['ukr', 'eng', 'rus']
clip_lang = lang[0]
d = dt.datetime.now()


def on_press(x, y, button, pressed):
    global first_x, first_y, second_x, second_y
    if pressed:
        first_x, first_y = x, y
    else:
        second_x, second_y = x, y


    if not pressed:
        # Stop listener
        return False


while True:
    try:
        if comb1.lower() != 'none' and k.is_pressed(comb1):
            now = str(d.day) + "_" + str(d.month) + "_" + str(d.year) + "__" + str(d.hour) + "__" + str(
                d.minute) + "__" + str(d.second)
            file_name = directory + now + '.png'
            pg.screenshot(file_name)
            print('Screnshot saved!')
            t.sleep(0.1)

        if comb2.lower() != 'none' and k.is_pressed(comb2):
            t.sleep(0.5)
            with Listener(on_click=on_press) as listener:
                listener.join()
            minim_x = min(first_x, second_x)
            maxim_x = max(first_x, second_x)

            minim_y = min(first_y, second_y)
            maxim_y = max(first_y, second_y)

            im = (ImageGrab.grab(bbox=(minim_x, minim_y, maxim_x, maxim_y)))
            if im.size != (0,0):
                print(F"First position ({minim_x,minim_y})")
                print(f"Second position ({maxim_x,maxim_y})")
                im.save(f'{dir_}\\t.png', 'PNG')
                tes = pytesseract.image_to_string(Image.open(f'{dir_}\\t.png'), lang=clip_lang)
                pclip.copy(tes)
                os.remove(f'{dir_}\\t.png')
                print('Copied to clipboard')
            else:
                print('Fail!')

        if comb3.lower() != 'none' and k.is_pressed(comb3):
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

        if comb4.lower() != 'none' and k.is_pressed(comb4):
            # change clip lang
            clip_lang = lang[(lang.index(clip_lang) + 1) % 3]
            print(f'Language: {clip_lang}')
            t.sleep(0.1)
    except:
        print('Fail!')
