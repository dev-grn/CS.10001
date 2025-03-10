from cs1robots import *

load_world('L02_04a.wld')
#load_world('L02_04b.wld')

hubo = Robot(beepers = 1)
hubo.set_pause(0.1)

def turn_right():
    for i in range(3):
        hubo.turn_left()

hubo.drop_beeper()
hubo.move()
while not hubo.on_beeper():
    if hubo.right_is_clear():
        turn_right()
        hubo.move()
    elif hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()
            