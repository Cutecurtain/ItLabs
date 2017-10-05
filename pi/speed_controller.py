

def get_speed_jerk(distance1, distance2, d_time):
    return (distance2 - distance1) / d_time


def get_velocity_2(velocity_1, speed_jerk, distance, max_distance):
    if distance < max_distance:
        return velocity_1 + speed_jerk
    else:
        return 0


def get_new_velocity_1(velocity_2, distance, min_distance, max_distance, max_speed):
    if min_distance <= distance < max_distance:
        return velocity_2
    elif distance >= max_distance:
        return max_speed
    elif distance < min_distance:
        return 0

