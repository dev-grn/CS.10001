from cs1robots import *

def turn_left(robot):
    robot.turn_left()

def turn_right(robot):
    i = 3
    while (i):
        robot.turn_left()
        i -= 1

def c_turn(sw, robot):
    if (robot._dir == 0):
        if robot.right_is_clear():
            turn_right(robot)
            robot.move()
            turn_right(robot)
        else:
            sw = False
    elif (robot._dir == 2):
        if robot.left_is_clear():
            turn_left(robot)
            robot.move()
            turn_left(robot)
        else:
            sw = False

def main():
    create_world()

    hubo = Robot(orientation = 'N', beepers = 1)
    hubo.set_pause(1)
    
    sw = True
    while (sw):
        if (hubo.front_is_clear()):
            hubo.move()
        else:
            c_turn(sw, hubo)

if __name__ == "__main__":
    main()
