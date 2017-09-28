from statistics import median
from nav import g

def filter_faulty_values(value):
    if value >= 3:
        return value
    return None


def get_filtered_sensor_value():
    values = []
    for i in range(10000):
        value = filter_faulty_values(g.can_ultra)
        if value is not None:
            values.append(value)
    return median(values)
