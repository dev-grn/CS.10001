from cs1robots import *

create_world()

# create a robot with one beeper
hubo = Robot(beepers = 1)
pause(1)

# move one step forward
hubo.move()
pause(1)

# turn left 90 degrees
hubo.turn_left()

# how to turn right?
