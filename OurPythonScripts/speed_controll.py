from nav import g
from sensor_logic import get_filtered_sensor_value
from distance_logic import optimal_speed

def adjust_to_optimal_speed():
    """adjut car speed based on current distance and current speed"""
    current_distance = get_filtered_sensor_value()
    print(current_distance)
    if current_distance != None:
        new_speed = optimal_speed(current_distance)
        if 0 < new_speed < 20:
            new_speed = 20
    else:
        new_speed = 0
    g.outspeedcm = new_speed

