from microbit import *
import radio

radio.on()
radio.config(channel=42)
radio.config(power=7)

command = None

dat = 0

while 1:
    x = radio.receive()
    if x != None:
        dat = x.split()
        x1 = (dat[0])
        # x2 = (dat[1])

    if x == "Press Command":
        command = 1
        print(x)
        display.show(Image.HAPPY)
        sleep(500)
        display.clear()
    else:
        pass

    if command == 1:
        x2 = (dat[1])
        if x1 == "ad":
            if x2 == "Hi":
                display.scroll("Hi")
                print("display = Hi")
        else:
            pass
