from microbit import *

import gc
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

initialize()
clear_oled()
gc.collect()


def servo(pin, degrees):
    degrees = max(0, min(degrees, 180))
    duty = degrees / 180 * 102 + 25
    pin.write_analog(duty)


while True:
    X = pin2.read_analog()
    VR = int(X * 180 / 1023)
    servo(pin8, VR)
    add_text(0, 2, "SERVO = " + (str(VR)))
    sleep(1000)
    add_text(0, 2, "           ")
    print("SERVO = " + str(VR))
    sleep(1000)
