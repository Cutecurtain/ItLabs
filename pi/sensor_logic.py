from statistics import median
from nav import g

#minimum distance for the distance sensor
min_dist = 0.10

#maximum distance for the distance sensor
max_dist = 2

#method for filetering values out of bounds
def filter_faulty_values(value):
	if min_dist < value < max_dist:
		return value
	return None


#number of values to calculate median from
median_range = 1000

#returns a median of a from the distance sensor
def get_filtered_sensor_value():
	values = []
	for i in range(median_range):
		value = filter_faulty_values(g.can_ultra)
		if value != None:
			values.append(value)
	if len(values) > 0:
		return median(values)
	return None
