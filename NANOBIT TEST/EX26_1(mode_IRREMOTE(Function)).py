from microbit import *
from AHT20 import *
from IRM import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

initialize()
clear_oled()
pin12.set_pull(pin12.PULL_UP)
a = AHT20()
d = IRM()
st_sw = 0
mode = 0
i2c.init(freq=100000, sda=pin20, scl=pin19)
addr=0x23

def lux():
    i2c.write(addr,bytes([0x10]))
    data = i2c.read(addr, 2)
    lux = (data[0]<<8 | data[1]) / (1.2)
    return lux
def sonar():
    sonar = pin1.read_analog()
    cm = sonar / 10
    return cm
def ir():
    key = d.get(pin12)
    global st_sw
    global mode
    if key != -1:
        print(key)
        if key == 2:
            st_sw = 0
            mode = 0
        if st_sw == 0:
            if key == 16:
                st_sw = 1
                mode = 1
            elif key == 17:
                st_sw = 1
                mode = 2
            elif key == 18:
                st_sw = 1
                mode = 3
            elif key == 20:
                st_sw = 1
                mode = 4
            else:
                pass
        else:
            pass
    else:
        pass
    return key, st_sw, mode
while 1:
    ir()
    if st_sw == 0:
        ir()
        clear_oled()
        add_text(0, 0, "1:Lux")
        add_text(0, 1, "2:Temp")
        add_text(0, 2, "3:Humid")
        add_text(0, 3, "4:ultra")
    elif st_sw == 1:
        ir()
        clear_oled()
        if mode == 1:
            light = lux()
            add_text(0, 2, "LUX = " + "{0:.2f}".format(light))
        elif mode == 2:
            t, h = a.read()
            add_text(0, 2, "Temp = " + "{0:.2f}".format(t))
        elif mode == 3:
            t, h = a.read()
            add_text(0, 2, "Humid = " + "{0:.2f}".format(h))
        elif mode == 4:
            s = sonar()
            add_text(0, 2, "Cm = " + "{0:.2f}".format(s))
        else:
            pass
    else:
        pass

