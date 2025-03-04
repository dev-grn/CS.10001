from cs1robots import *

def turn_left(robot):
    robot.turn_left()

def turn_right(robot):
    i = 3
    while (i):
        robot.turn_left()
        i -= 1

def move_d(robot, i):
    while (i):
        robot.move()
        turn_right(robot)
        robot.move()
        turn_left(robot)

        if (robot.on_beeper()):
            robot.pick_beeper()

        i -= 1

def main():
    create_world(avenues=12, streets=12)
    #load_world('worlds/harvest2.wld')

    hubo = Robot(orientation = 'N', beepers = 1)
    hubo.set_pause(1)

    hubo.set_trace(color = "Black")
    
    i = 6
    while (i):
        hubo.move()
        i -= 1

    if (hubo.on_beeper()):
        hubo.pick_beeper()

    # Starting the diamond pickup
    i = 5
    move_d(hubo, i)
    turn_right(hubo)
    while (i):
        move_d(hubo, i)
        turn_right(hubo)
        move_d(hubo, i)
        turn_right(hubo)
        i -= 1

if __name__ == "__main__":
    main()
