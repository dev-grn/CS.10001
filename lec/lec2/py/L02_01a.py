from cs1robots import *

load_world('L02_01.wld')    # load a pre-configured world
hubo = Robot(beepers = 0)
hubo.set_pause(0.5)     # to tell hubo to pause beteen movements

def move_and_pick():  
    hubo.move()
    hubo.pick_beeper()

for i in range(9):  
    pause(1)
    move_and_pick()