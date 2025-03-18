from cs1robots import *

load_world("L02_03.wld")

hubo = Robot(beepers = 0)
hubo.set_pause(1)

while not hubo.on_beeper():
    hubo.move()