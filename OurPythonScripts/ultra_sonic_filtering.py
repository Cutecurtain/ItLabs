import statistics


def get_median(values):
    return statistics.median(values)


def filter_faulty_values(value):
    if value >= 3:
        return value
    return None


def get_sensor_values():
    values = []
    for i in range(10000):
        value = filter_faulty_values(g.can_ultra)
        if value is not None:
            values.append(value)
    return get_median(values)
