from cs1robots import *

def turn_left(robot):
    robot.turn_left()

def turn_right(robot):
    i = 3
    while (i):
        robot.turn_left()
        i -= 1

def move(robot):
    robot.move()
    if (robot.on_beeper()):
        robot.pick_beeper()

def mr(robot, i):
    while (i):
        move(robot)
        i -= 1
        
    turn_left(robot)

def main(): 
    create_world()
    #load_world('worlds/harvest1.wld')

    hubo = Robot(beepers = 1)
    hubo.set_pause(1)

    i = 6
    mr(hubo, 6)

    while (i):
        mr(hubo, i)
        mr(hubo, i)
        i -= 1


if __name__ == "__main__":
    main()
