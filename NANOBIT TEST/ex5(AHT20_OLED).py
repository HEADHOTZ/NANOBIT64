from microbit import i2c,sleep
from AHT20 import *
import gc
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

initialize()
clear_oled()
gc.collect()

a = AHT20()
while 1:
    sleep(1000)
    t,h = a.read()
    print(type(t))
    add_text(0, 1,"Temp = " + str(t))
    add_text(0, 2,"humi = " + str(h))
    print("Temp = ", t)
    print("humidity = ",h)
    sleep(500)
