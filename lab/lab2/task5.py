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
    r = Robot(orientation = 'N', beepers = 1)
    r.set_pause(0.2)

    return r

def main(c = 10, s = 10):
    r = setup(c, s)
    while (r.front_is_clear() or r.right_is_clear() or r.left_is_clear()):
        if (r.front_is_clear()):
            mv(r, s - 1)
        elif (r.right_is_clear() and r._dir == 0):
            tr(r)
            mv(r)
            tr(r)
        else:
            tl(r)
            mv(r)
            tl(r)

if __name__ == "__main__":
    main()
