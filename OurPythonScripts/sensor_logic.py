from statistics import median
from nav import g

def filter_faulty_values(value, *, min_dist=0.10, max_dist=2):
	"""Filter out values out of bounds."""
	if min_dist < value < max_dist:
		return value
	return None

def get_filtered_sensor_value(range=1000):
	"""Return a median from the distance sensor."""
	values = []
	for i in range(range):
		value = filter_faulty_values(g.can_ultra)
		if value != None:
			values.append(value)
	if len(values) > 0:
		return median(values)
	return None
