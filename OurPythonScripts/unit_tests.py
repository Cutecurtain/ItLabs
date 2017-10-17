from distance_logic import optimal_speed
from sensor_logic import get_filtered_sensor_value, g


def test_sensor_filter():
    assert get_filtered_sensor_value() == None
    g.can_ultra = 1
    assert get_filtered_sensor_value() == 1
    g.can_ultra = 3 
    assert get_filtered_sensor_value() == None

def test_optimal_speed():
    assert optimal_speed(-10) == 0
    assert optimal_speed(50) == 40

def test_speed_control():
    assert False

test_optimal_speed()
test_sensor_filter()
#test_speed_control()
