from microbit import *
from AHT20 import *
from iled4 import *
from IRM import *
import music
import gc
gc.collect()
a = AHT20()
f = iled4()
addr = 0x23
mode = 0
st_sw = 0
x = ''
esc = pin12
enter = pin8
ch = ["t","T","H","U","L","R"]
i2c.init(freq=100000, sda=pin20, scl=pin19) # ตอน Test ปิดตรงนี้แต่ยังทำงานได้ถ้าลองทำอีกรอบลองเปิดไว้ดู(lux)

def lux():
    i2c.write(addr,bytes([0x10]))
    data = i2c.read(addr, 2)
    lux = (data[0]<<8 | data[1]) / (1.2)
    return lux

f.clear()
while 1:
    t,h = a.read()
    temp = temperature()
    ultra = pin1.read_analog()/10
    light = lux()
    mode = int((pin2.read_analog()*4/1023)+1)
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
            print(temp)
            f.print(temp)
            f.update_display()
        elif mode == 2:
            print(t)
            x = int(t*100)
            f.print(x)
            f.set_decimal(1)
            f.update_display()
        elif mode == 3:
            print(h)
            x = int(h*100)
            f.print(x)
            f.set_decimal(1)
            f.update_display()
        elif mode == 4:
            print(ultra)
            x = int(ultra*10)
            f.print(x)
            f.set_decimal(2)
            f.update_display()
        elif mode == 5:
            print(int(light))
            f.print(int(light))
            f.update_display()
            sleep(500)
        else:
            pass
    else:
        pass
