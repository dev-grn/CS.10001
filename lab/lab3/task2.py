from cs1robots import *

def setup(w = None):
    if (w == None):
        create_world()
    else:
        load_world(w)
    r = Robot(beepers = 0)
    r.set_pause(0.1)

    return r

def mv(r, i = 1):
    while (i):
        while (r.on_beeper()):
            r.pick_beeper()
        r.move()
        i -= 1

def tr(r):
    i = 3
    while (i):
        r.turn_left()
        i -= 1

def main(a):
    r = setup(a)
    i = 0
    while (r.front_is_clear()):
        mv(r)
        i += 1
    while (r.on_beeper()):
        r.pick_beeper()
    for j in range(2):
        r.turn_left()
    for j in range(i):
        r.move()
    tr(r)
    r.move()
    while (r.carries_beepers()):
        r.drop_beeper()
    for j in range(2):
        r.turn_left()
    r.move()


if __name__ == "__main__":
    for w in range(2):
        main('worlds/trash{}.wld'.format(w + 1))
        if (1 - w):
            import cs1robots
            cs1robots._scene._forceClose()
            cs1robots._scene = None
            cs1robots._world = None
