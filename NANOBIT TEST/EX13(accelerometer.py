from microbit import *
while True:
    reading_X = accelerometer.get_x()
    reading_Y = accelerometer.get_y()
    reading_Z = accelerometer.get_z()

    display.scroll("X = " + str(reading_X), 100)
    display.scroll("Y = " + str(reading_Y), 100)
    display.scroll("Z = " + str(reading_Z), 100)

    print("X = " + str(reading_X))
    print("Y = " + str(reading_Y))
    print("Z = " + str(reading_Z))
