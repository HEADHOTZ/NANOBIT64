from microbit import *
from microbit import sleep
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
initialize()
clear_oled()

while True:
    sonar = pin1.read_analog()
    cm = sonar / 10
    # display.scroll('cm = ' + str(cm), 100)
    add_text(0, 2, "          ")
    add_text(0, 2, "CM = " + str(cm))
    print('RAW = ', sonar, 'CM = ', cm)
    sleep(1000)
