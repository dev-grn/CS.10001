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
    r = Robot(beepers=100, avenue=2, street=6, orientation='E')
    r.set_pause(0.1)

    return r

def cl(r):
    tl(r)
    if not (r.front_is_clear()):
        tr(r)
        return 'wall'
    else:
        orient = r._dir
        mv(r)
        # if (r.front_is_clear()):
        tl(r)
        if (r.front_is_clear()):
            tr(r)
            tr(r)
            if (r.front_is_clear()):
                tr(r)
                mv(r)
                tl(r)
                return 'window'
        # print(orient)
        while not (r._dir == (orient + 2) % 4):
            tl(r)
        # print(r._dir)
        mv(r)
        tl(r)
        return 'lturn'
                

def main(w):
    r = setup(w)
    # enter
    mv(r)
    tl(r)

    # start with single move, keep the coordinates
    x, y = r._x, r._y
    mv(r)

    # trace outside
    while not ((r._x == x) and (r._y == y)):
        if (r.front_is_clear()):
            vv = cl(r)
            print(vv)
            if (vv == 'wall'):
                mv(r)
            elif (vv == 'lturn'):
                tl(r)
                mv(r)
            elif (vv == 'window'):
                r.drop_beeper()
                mv(r)
            else:
                mv(r)
        else:
            tr(r)

if __name__ == "__main__":
    for w in range(2):
        main('worlds/rain{}.wld'.format(w + 1))
        if (1 - w):
            import cs1robots
            cs1robots._scene._forceClose()
            cs1robots._scene = None
            cs1robots._world = None

    # main('worlds/rain2.wld')
