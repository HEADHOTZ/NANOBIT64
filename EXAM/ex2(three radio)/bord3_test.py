from microbit import *
import radio

radio.on()
radio.config(channel=42)
radio.config(power=7)

while 1:
    x = radio.receive()
    if x != None:
        if x == "adHi":
            display.scroll("Hi")
