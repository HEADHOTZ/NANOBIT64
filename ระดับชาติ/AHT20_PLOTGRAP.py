from microbit import *
from AHT20 import *
import time
a = AHT20()
while 1:
    t, h = a.read()
    print((t, h))
