from microbit import *

i2c.init(freq=100000, sda=pin20, scl=pin19)
addr = 0x23
def lux():
    i2c.write(addr,bytes([0x10]))
    data = i2c.read(addr, 2)
    lux = (data[0]<<8 | data[1]) / (1.2)
    return lux

while 1:
    light = lux()
    print((light,))
    sleep(500)
