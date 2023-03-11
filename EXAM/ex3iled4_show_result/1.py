from microbit import *

from iled1 import *

from AHT20 import *
import music
enter = pin8
esc = pin13
f = iled4()
a = AHT20()
mode = 0
st_sw = 0
ch = ["t","T","H","U","L"]
while 1:
    t,h = a.read()
    mode = int(pin2.read_analog()*(5/1024)+1)
    # check sw esc
    if not esc.read_digital():
        while not esc.read_digital():
            sleep(10)
        st_sw = 0
        music.pitch(2000, 200)
    # check sw enter
    if not enter.read_digital():
        while not enter.read_digital():
            sleep(10)
        st_sw = 1
        music.pitch(2000, 200)
    if st_sw == 0:
        display.show(ch[mode-1])
        f.clear()
    if st_sw == 1:
        display.clear()
        if mode == 1:
            display.show(ch[mode-1])
            f.print(temperature())
            f.update_display()
        elif mode == 2:
            display.clear()
            display.show(ch[mode])
            for i in range(2):
                print(t)
                """
                f.write_digit(i,0)
                f.set_decimal(1)
                f.update_display()
                """
