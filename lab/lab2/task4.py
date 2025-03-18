a = ['worlds/harvest1.wld', 'worlds/harvest3.wld', 'worlds/harvest4.wld']

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
        while (r.on_beeper()):
            r.pick_beeper()
        r.move()
        i -= 1

def setup(w = None):
    if (w == None):
        create_world()
    else:
        load_world(w)
    r = Robot(beepers = 1)
    r.set_pause(0.2)

    return r

def main(w = None):
    r = setup(w)

    mv(r)
    i = 3
    j = 2
    while (i):
        mv(r, 5)
        tl(r)
        mv(r)
        tl(r)
        mv(r, 5)
        if (j):
            tr(r)
            mv(r)
            tr(r)
        i -= 1
        j -= 1

if __name__ == "__main__":
    i = 2
    for w in a:
        main(w)
        if (i):
            import cs1robots
            cs1robots._scene._forceClose()
            cs1robots._scene = None
            cs1robots._world = None
        i -= 1
