from ctypes import *

import time

msvcrt = cdll.msvcrt
counter = 0


while 1:
    counter += 1
    msvcrt.printf("Loop iteration {:d}\n".format(counter).encode("utf-8"))

    time.sleep(2)



