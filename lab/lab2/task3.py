a = ['worlds/hurdles1.wld', 'worlds/hurdles2.wld', 'worlds/hurdles3.wld']

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

def setup(w = None):
    if (w == None):
        create_world()
    else:
        load_world(w)
    r = Robot(beepers = 1)
    r.set_pause(0.2)

    return r

def jump_one_hurdle(r):
    tl(r)
    mv(r)
    tr(r)
    mv(r)
    tr(r)
    mv(r)
    tl(r)

def main(w = None):
    r = setup(w)

    while not (r.on_beeper()):
        if (r.front_is_clear()):
            mv(r)
        else:
            jump_one_hurdle(r)

    r.pick_beeper()

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
