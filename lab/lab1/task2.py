from cs1robots import *

def turn_left(robot):
    robot.turn_left()

def turn_right(robot):
    i = 3
    while (i):
        robot.turn_left()
        i -= 1

def jump(robot):
    robot.move()
    turn_left(robot)
    robot.move()
    turn_right(robot)
    robot.move()
    turn_right(robot)
    robot.move()
    turn_left(robot)

def main(): 
    create_world()
    #load_world('worlds/hurdles1.wld')

    hubo = Robot(beepers = 1)
    hubo.set_pause(1)
    
    i = 4
    while (i):
        jump(hubo)
        i -= 1

    hubo.move()
    hubo.pick_beeper()

if __name__ == "__main__":
    main()
