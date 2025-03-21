from cs1robots import *

def tl(r):
    r.turn_left()

def tr(r):
    i = 3
    while (i):
        r.turn_left()
        i -= 1

def mv(r, i = 1):
    while (i):
        r.move()
        i -= 1

def setup(c = 10, r = 10, w = None):
    if (w == None):
        create_world(avenues = c, streets = r)
    else:
        load_world(w)
    r = Robot(beepers = 1)
    r.set_pause(0.2)

    return r
