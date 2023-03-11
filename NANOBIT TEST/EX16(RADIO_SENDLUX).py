from microbit import *
import radio
radio.on()
radio.config(channel = 42)
radio.config(power = 7)
dat = 0
# บอร์ด 3 E:
i2c.init(freq=100000, sda=pin20, scl=pin19)
addr = 0x23
x1 = ''
while True:
    x = radio.receive()

    i2c.write(addr, bytes([0x10]))
    sleep(120)
    data = i2c.read(addr, 2)
    lux = (data[0]<<8 | data[1]) / (1.2)

    if x != None:
        dat = x.split(",")
        x1 = (dat[0])

    if x1 == 'L':
        display.show(x1)
        msg = str(lux)
        radio.send(msg)
        print(lux)
    else:
        display.clear()


