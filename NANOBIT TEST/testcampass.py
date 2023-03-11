from microbit import *
D = ['N', 'NW', 'W', 'SW', 'S', 'SE', 'E', 'NE']

while True:
    angle = compass.heading()
    if angle < 45:
        D = 'N'

    elif angle < 135:
        D = 'E'

    elif angle < 225:
        D = 'S'

    elif angle < 315:
        D = 'W'
    else:
        D = 'N'
    display.show(D)
