from cs1robots import *

def turn_left(robot):
    robot.turn_left()

def turn_right(robot):
    i = 3
    while (i):
        robot.turn_left()
        i -= 1

def stair_m(robot):
    robot.move()
    turn_left(robot)
    robot.move()
    turn_right(robot)
    robot.move()

def main():
    create_world()
    #load_world('worlds/newspaper.wld')

    hubo = Robot(beepers = 1)
    hubo.set_pause(1)

    i = 4
    while (i):
        stair_m(hubo)
        i -= 1

    hubo.move()
    if (hubo.on_beeper()):
        hubo.pick_beeper()
    turn_left(hubo)
    turn_left(hubo)
    hubo.move()

    i = 4
    while (i):
        stair_m(hubo)
        i -= 1

if __name__ == "__main__":
    main()
