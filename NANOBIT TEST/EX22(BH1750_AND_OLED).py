from microbit import *
import gc
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

i2c.init(freq=100000, sda=pin20, scl=pin19)
addr = 0x23

initialize()
clear_oled()
gc.collect()

while True:
    i2c.write(addr, bytes([0x10]))
    sleep(120)
    data = i2c.read(addr, 2)
    lux = (data[0] << 8 | data[1]) / (1.2)
    add_text(0, 2, "LUX = " + "{0:.2f}".format(lux))
    # add_text(0, 2, "LUX = " + str(lux))
    # print("LUX = " + ('%.2f'(str(lux))))
    print("LUX = " + "{0:.2f}".format(lux))
    sleep(1000)
