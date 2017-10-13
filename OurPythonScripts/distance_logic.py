
#returns optimal speed based on current distance to car in front
def optimal_speed(current_distance):
	speed = current_distance * 100 - 100
	if (speed > 40):
		speed = 40
	if (speed < 0):
		speed = 0
	return speed
	
