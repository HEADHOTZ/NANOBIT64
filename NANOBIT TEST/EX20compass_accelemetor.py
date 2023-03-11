from microbit import *

Mode = ''
D = ['N', 'NW', 'W', 'S', 'SW', 'SE', 'E', 'NE']

while True:
    get_X = accelerometer.get_x()
    get_Y = accelerometer.get_y()
    get_Z = accelerometer.get_z()
    get_XYZ = accelerometer.get_values()

    X = get_X / 256
    Y = get_Y / 256
    Z = get_Z / 256

    if button_a.was_pressed():
        Mode = 'C'

        display.show('C')
        sleep(500)
        display.clear()

    if button_b.was_pressed():
        Mode = 'A'

        display.show('A')
        sleep(500)
        display.clear()

    if Mode == 'C':
        angle = compass.heading()
        angle = int(angle/45)
        display.show(D[angle])
        sleep(500)

    if Mode == 'A':
        if X < 0:
            X = 0
        if X > 4:
            X = 4

        if Y < 0:
            Y = 0
        if Y > 4:
            Y = 4

        sleep(100)
        display.clear()
        display.set_pixel(int(X), int(Y), 9)
