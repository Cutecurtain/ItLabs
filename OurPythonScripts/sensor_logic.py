from statistics import median
from nav import g

def filter_faulty_values(value, min_distance, max_distance):
    if min_distance <= value <= max_distance:
        return value
    else:
        return 0


def get_filtered_sensor_value(n_updates, min_distance, max_distance):
    values = []
    for i in range(n_updates):
        value = filter_faulty_values(g.can_ultra * 100, min_distance, max_distance)
        if value is not None:
            values.append(value)
    if values.count() > 0:
        return median(values)
    else:
        return None
