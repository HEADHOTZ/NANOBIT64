from microbit import *
while True:
    angle = compass.heading()
    display.scroll(str(angle))
    print (angle)
    sleep(100)
