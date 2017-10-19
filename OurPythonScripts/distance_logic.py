
def optimal_speed(current_distance):
	"""Return optimal speed based on current distance to car in front."""
	speed = current_distance * 250 - 100
	if (speed > 40):
		speed = 40
	if (speed < 0):
		speed = 0
	return speed
	
