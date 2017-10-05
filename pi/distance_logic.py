
min_dist = 10 #cm

#should be adjusted  
distance_scaling = 1.1

#def optimal_distance(current_speed):
#	return min_dist + distance_scaling * current_speed

def optimal_speed(current_distance):
	speed = current_distance * 500 - 100
	if (speed > 100):
		speed = 100
	if (speed < -100):
		speed = -100
	return speed
	
