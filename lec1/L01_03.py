from cs1robots import *

create_world()

hubo = Robot(beepers = 1)
hubo.set_pause(1)

def turn_right():
	hubo.turn_left()
	hubo.turn_left()
	hubo.turn_left()

def turn_around():
	hubo.turn_left()
	hubo.turn_left()

def climb_up_four_stairs():
	climb_up_one_stair()
	climb_up_one_stair()
	climb_up_one_stair()
	climb_up_one_stair()

def climb_up_one_stair():
	hubo.turn_left()
	hubo.move()
	turn_right()
	hubo.move()
	hubo.move()

climb_up_four_stairs()
hubo.drop_beeper()
turn_around()
#climb_down_four_stairs()
