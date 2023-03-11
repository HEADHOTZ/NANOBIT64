from AHT20 import *
from IRM import *
from iled4 import *
import gc
from microbit import *
import music
gc.collect()

a = AHT20()
f = iled4()
d = IRM()
addr = 0x23
mode = 0
st_sw = 0
n = 0
esc = pin12
enter = pin8
ir = pin13.set_pull(pin13.PULL_UP)
ch = ["t","T","H","U","L","R"]
i2c.init(freq=100000, sda=pin20, scl=pin19)

f.clear()
while 1:
    mode = int((pin2.read_analog()*6/1023)+1)
    if mode == 7:
        mode -= 1
    if not esc.read_digital():
        while not esc.read_digital():
            sleep(10)
        music.pitch(2000,100)
        st_sw = 0
    elif not enter.read_digital():
        while not enter.read_digital():
            sleep(10)
        music.pitch(2000,100)
        st_sw = 1
    else:
        pass
    if st_sw == 0:
        display.show(ch[mode-1])
        f.clear()
    elif st_sw == 1:
        if mode == 1:
            temp = temperature()
            print(temp)
            f.print(temp)
            f.update_display()
        elif mode == 2:
            t,h = a.read()
            print(t)
            x = int(t*100)
            f.print(x)
            f.set_decimal(1)
            f.update_display()
        elif mode == 3:
            t,h = a.read()
            print(h)
            x = int(h*100)
            f.print(x)
            f.set_decimal(1)
            f.update_display()
        elif mode == 4:
            ultra = (pin1.read_analog()/10)
            print(ultra)
            f.print(int(ultra*10))
            f.set_decimal(2)
            f.update_display()
            sleep(500)
        elif mode == 5:
            i2c.write(addr,bytes([0x10]))
            data = i2c.read(addr, 2)
            lux = (data[0]<<8 | data[1]) / (1.2)
            print(int(lux))
            f.print(int(lux))
            f.update_display()
            sleep(500)
        elif mode == 6:
            key = d.get(pin13)
            if key != -1:
                if key == 22:
                    n = 0
                elif key == 12:
                    n = 1
                elif key == 24:
                    n = 2
                elif key == 94:
                    n = 3
                elif key == 8:
                    n = 4
                elif key == 28:
                    n = 5
                elif key == 90:
                    n = 6
                elif key == 66:
                    n = 7
                elif key == 82:
                    n = 8
                elif key == 74:
                    n = 9
                print(key)
                f.print(n)
                f.update_display()
        else:
            pass
    else:
        pass
