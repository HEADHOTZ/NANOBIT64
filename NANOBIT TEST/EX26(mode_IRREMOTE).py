import gc
gc.collect()
from IRM import *
from microbit import *
from AHT20 import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text
pin12.set_pull(pin12.PULL_UP)
mode = 0
st_sw = 0
number = 0
key = 0
a = AHT20()
d = IRM()
initialize()
clear_oled()
i2c.init(freq=100000, sda=pin20, scl=pin19)
addr=0x23

def lux():
    i2c.write(addr,bytes([0x10]))
    data = i2c.read(addr, 2)
    lux = (data[0]<<8 | data[1]) / (1.2)
    return lux
def check_key():
    key = d.get(pin12)
    # if key != -1 or st_sw == 1:  // ต้องลอง test ดู
    if key != -1:
        if key == 2:
            st_sw = 0
            mode = 0
        if key == 16:
            st_sw = 1
            mode = 1
    return(st_sw, mode)

def menu():
    if st_sw == 0:
        clear_oled()
        add_text(0, 0, "1:Temp")
        add_text(0, 1, "2:Humid")
        add_text(0, 2, "3:Lux")
        add_text(0, 3, "4:ultra")

def mode():

while 1:
    key = d.get(pin12)
    print(key)
    if key != -1:
        print(key)
        if key == 2:
            st_sw = 0
            mode = 0
        else:
            pass
        if st_sw == 0:
            clear_oled()
            add_text(0, 0, "1:Temp")
            add_text(0, 1, "2:Humid")
            add_text(0, 2, "3:Lux")
            add_text(0, 3, "4:ultra")
            if key == 16:
                mode = 1
                st_sw = 1
            elif key == 17:
                mode = 2
                st_sw = 1
            elif key == 18:
                mode = 3
                st_sw = 1
            elif key == 20:
                mode = 4
                st_sw = 1
            else:
                pass
        else:
            pass
    else:
        pass
    if key != -1:
        print(key)
        if st_sw == 1:
            if key != -1:
                if key == 2:
                    st_sw = 0
                    mode = 0
            while mode == 1:
                key = d.get(pin12)
                if key == 2:
                    break
                t, h = a.read()
                clear_oled()
                add_text(0, 2, "Temp = " + "{0:.2f}".format(t))
            while mode == 2:
                key = d.get(pin12)
                if not pin12.read_digital():
                    st_sw = 0
                    mode = 0
                clear_oled()
                t, h = a.read()
                add_text(0, 2, "Humid = " + "{0:.2f}".format(h))
                print(key)
            while mode == 3:
                key = d.get(pin12)
                if not pin12.read_digital():
                    st_sw = 0
                    mode = 0
                clear_oled()
                light = lux()
                add_text(0, 2, "LUX = " + "{0:.2f}".format(light))
                print(key)
            while mode == 4:
                key = d.get(pin12)
                if not pin12.read_digital():
                    st_sw = 0
                    mode = 0
                clear_oled()
                sonar = pin1.read_analog()
                cm = sonar / 10
                add_text(0, 2, "Cm = " + "{0:.2f}".format(cm))
                print(key)
            else:
                pass
    else:
        pass
