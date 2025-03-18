from cs1robots import *

def r(hubo):
    while not (hubo.facing_north()):
        hubo.turn_left()
    hubo.turn_left()

    while not (hubo._x == 1):
        hubo.move()
    hubo.turn_left()
    while not (hubo._y == 1):
        hubo.move()

def setup(c = 10, r = 10, w = None, o = 'W', a = 9, s = 3):
    if (w == None):
        create_world(avenues = c, streets = r)
    else:
        load_world(w)
    r = Robot(orientation = o, avenue = a, street = s)
    r.set_pause(0.1)

    return r

def main():
    hubo = setup()
    r(hubo)

if __name__ == "__main__":
    main()
