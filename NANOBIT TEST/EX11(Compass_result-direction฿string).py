from microbit import *
D = ['N', 'NW', 'W', 'S', 'SW', 'SE', 'E', 'NE']

"""
D = [Image.ARROW_N, Image.ARROW_NW, Image.ARROW_W, Image.ARROW_SW,
    Image.ARROW_S, Image.ARROW_SE, Image.ARROW_E, Image.ARROW_NE]
    เก็บค่าทิศเป็นเข็มทิศทาง
    """

while True:
    angle = compass.heading()
    angle = int(angle/45)
    display.scroll(D[angle])
