
import time
import sensor_logic as sl
from nav import g

def get_speed_jerk(min_distance, max_distance):
    distance_1 = sl.get_filtered_sensor_value(10000, min_distance, max_distance)
    start = time.time()
    distance_2 = sl.get_filtered_sensor_value(10000, min_distance, max_distance)
    end = time.time()
    return (distance_2 - distance_1) / (end - start)


def get_velocity_2(distance, min_distance, max_distance):
    if distance <= max_distance:
        return g.outspeedcm + get_speed_jerk(min_distance, max_distance)
    else:
        return 0


def get_new_velocity_1(min_distance, max_distance, max_speed):
    distance = sl.get_filtered_sensor_value(10000, min_distance, max_distance)
    if min_distance <= distance <= max_distance:
        return get_velocity_2(distance, min_distance, max_distance)
    elif distance >= max_distance:
        return max_speed
    elif 0 < distance < min_distance:
        return 0


