from cs1robots import *

def setup(w = None):
    if (w == None):
        create_world()
    else:
        load_world(w)
    r = Robot(beepers = 0)
    r.set_pause(0.1)

    return r

def R(hubo):
    while not (hubo.facing_north()):
        hubo.turn_left()
    hubo.turn_left()

    while not (hubo._x == 1):
        hubo.move()
    hubo.turn_left()
    while not (hubo._y == 1):
        hubo.move()

def mv(r, i = 1):
    while (i):
        r.move()
        while (r.on_beeper()):
            r.pick_beeper()
        i -= 1

def tl(r):
    r.turn_left()

def tr(r):
    i = 3
    while (i):
        r.turn_left()
        i -= 1

def main(a):
    r = setup(a)

    while (True):
        if (r.front_is_clear()):
            mv(r)
        else:
            if (r._dir == 3):
                tl(r)
                if not (r.front_is_clear()):
                    break
                mv(r)
                tl(r)
            else:
                tr(r)
                if not (r.front_is_clear()):
                    break
                mv(r)
                tr(r)
    R(r)
    while (r.carries_beepers()):
        r.drop_beeper()


if __name__ == "__main__":
    for w in range(2):
        main('worlds/trash{}.wld'.format(w + 3))
        if (1 - w):
            import cs1robots
            cs1robots._scene._forceClose()
            cs1robots._scene = None
            cs1robots._world = None
