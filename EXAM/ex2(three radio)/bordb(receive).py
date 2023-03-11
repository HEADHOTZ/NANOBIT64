from microbit import *
import radio

radio.on()
radio.config(channel=42)
radio.config(power=7)

def servo(pin, degrees):
    degrees = max(0, min(degrees, 180))
    duty = degrees / 180 * 102 + 25
    pin.write_analog(duty)

while 1:

    x = radio.receive()
    if x != None:
        if x[0:2] == "bs":
            servo(pin8, int(x[2:5]))
        if x[0:2] == "bd":
            display.scroll("Hi")

