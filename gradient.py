from colour import Color
import colorit
# import pickle
# from PIL import Image
from PIL import ImageColor
import time

n = 120
n2 = int(n / 3)
conv = lambda h: ImageColor.getcolor(h, 'RGB')

a = Color('blue')
colors1 = list(a.range_to(Color('cyan'), n2))

a = Color('cyan')
colors2 = list(a.range_to(Color('purple'), n2))

a = Color('purple')
colors3 = list(a.range_to(Color('blue'), n2))

colors = [*colors1, *colors2, *colors3]
colors = [conv(c.hex) for c in colors]
#
# with open('colors.txt', 'wb') as f:
#     pickle.dump(colors, f)

def rainbow_text(message,color_steps=50 ,time_=1):
    # with open('colors.txt','rb') as f:
    #     colors = pickle.load(f)

    # generate a list of colors that smoothly transition through the rainbow spectrum
    color_range = len(colors) - 1
    color_transition = []
    for i in range(color_range):
        start_color = colors[i]
        end_color = colors[i+1]
        for step in range(color_steps):
            r = int(start_color[0] + (float(step)/color_steps)*(end_color[0]-start_color[0]))
            g = int(start_color[1] + (float(step)/color_steps)*(end_color[1]-start_color[1]))
            b = int(start_color[2] + (float(step)/color_steps)*(end_color[2]-start_color[2]))
            color_transition.append((r, g, b))
    start = time.time()
    while time.time()-start <= time_:
        for char in message:
            color = color_transition.pop(0)
            color_transition.append(color)
            print(colorit.color_front(char, *color), end='')
        time.sleep(0.1)
        print('\r', end='')

    for char in message:
        color = color_transition.pop(0)
        color_transition.append(color)
        print(colorit.color_front(char, *color), end='')
    print()

# im = Image.new('RGB', (n, 1))
# ld = im.load()
# x = 0
# y = 0
# for c in colors:
#     r, g, b = conv(c)
#     ld[x, y] = (r, g, b)
#     x += 1
#
# im.save('t.png', 'PNG')



