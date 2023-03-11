from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_stamp import draw_stamp
from ssd1306_img import create_stamp

initialize()
clear_oled()

image_1 = create_stamp(Image.HEART)
image_2 = create_stamp(Image.HEART_SMALL)
image_3 = create_stamp(Image.DIAMOND)
image_4 = create_stamp(Image.DIAMOND_SMALL)
image_5 = create_stamp(Image.PACMAN)

while True:
    VR = int(pin2.read_analog() * 6 / 1024)
    if VR == 1:
        clear_oled()
#       draw_stamp(x, y, stamp, color, draw=1)
        draw_stamp(20, 20, image_1, 1)
    if VR == 2:
        clear_oled()
        draw_stamp(20, 20, image_2, 1)
    if VR == 3:
        clear_oled()
        draw_stamp(20, 20, image_3, 1)
    if VR == 4:
        clear_oled()
        draw_stamp(20, 20, image_4, 1)
    if VR == 5:
        clear_oled()
        draw_stamp(20, 20, image_5, 1)
    else:
        clear_oled()
    print(VR)


