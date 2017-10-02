from statistics import median
from nav import g

def filter_faulty_values(value, minimum_distance, maximum_distance):
	if minimum_distance < value < maximum_distance:
		return value
	return 0


def get_filtered_sensor_value(minimum_distance, maximum_distance):
	values = []
	for i in range(10000):
		value = filter_faulty_values(g.can_ultra, minimum_distance, maximum_distance)
		if value > 0:
			values.append(value)
	if len(values) > 0:
		return median(values)
	return 0