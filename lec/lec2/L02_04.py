from cs1robots import *

#load_world("L02_04.wld")
load_world("L02_04a.wld")

hubo = Robot(beepers = 1)
hubo.set_pause(0.2)

hubo.drop_beeper()
hubo.move()
while not hubo.on_beeper():
    if hubo.front_is_clear():
        hubo.move()
    else:
        hubo.turn_left()