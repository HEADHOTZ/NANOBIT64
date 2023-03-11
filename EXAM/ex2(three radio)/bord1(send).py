from microbit import *
import radio
import neopixel

# Drive F
radio.on()
radio.config(channel=42)
radio.config(power=7)

np = neopixel.NeoPixel(pin10, 16)

color = [
    (255, 255, 255),
    (255, 0, 0),
    (255, 255, 0),
    (0, 255, 0),
    (128, 0, 255),
    (255, 128, 0),
    (0, 255, 255),
]

Num = 0


def servo(pin, degrees):
    degrees = max(0, min(degrees, 180))
    duty = degrees / 180 * 102 + 25
    pin.write_analog(duty)


while 1:
    # BordA----------------------
    VR = pin2.read_analog()
    x = input("Press Command : ")
    try:
        if x[0] == "a":
            if x[1] == "s":
                if int(x[2:5]) == 180:
                    print("servo = {}".format(x[2:5]))
                    radio.send(x)
                if int(x[2:5]) >= 0 and int(x[2:5]) < 180:
                    print("servo = {}".format(x[2:5]))
                if int(x[2:5]) > 180:
                    print("Out of range")
            elif x[1] == "d":
                if x[2:4] == "Hi":
                    radio.send(x)
                    print("Display = Hi")
        else:
            pass

        if x[0] == "b":
            if x[1] == "s":
                if int(x[2:5]) == 180:
                    print("servo = {}".format(x[2:5]))
                    radio.send(x)
                if int(x[2:5]) >= 0 and int(x[2:5]) < 180:
                    print("servo = {}".format(x[2:5]))
                if int(x[2:5]) > 180:
                    print("Out of range")
            elif x[1] == "d":
                if x[2:4] == "Hi":
                    radio.send(x)
                    print("Display = Hi")
        else:
            pass
    except:
        pass
    # Bord MAIN----------------------
