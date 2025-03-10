from cs1robots import *

create_world(3, 3)

hubo = Robot(beepers = 100)
hubo.set_pause(0.5)

def dance():
    for i in range(4):
        hubo.turn_left()
        pause(0.2)

def move_or_turn():
    if hubo.front_is_clear():
        dance()
        hubo.move()
    else:
        hubo.turn_left()
        hubo.drop_beeper()

for i in range(18):
    move_or_turn()

