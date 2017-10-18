from distance_logic import optimal_speed
from nav import g
from sensor_logic import get_filtered_sensor_value
from speed_controll import adjust_to_optimal_speed

def test_sensor_filter():
    g.can_ultra = -200
    assert get_filtered_sensor_value() == None
    g.can_ultra = 1
    assert get_filtered_sensor_value() == 1
    g.can_ultra = 3 
    assert get_filtered_sensor_value() == None

def test_optimal_speed():
    assert optimal_speed(-10) == 0
    assert optimal_speed(50) == 40

def test_speed_control():
    g.can_ultra = 2
    adjust_to_optimal_speed()
    assert g.outspeedcm <= 40
    g.can_ultra = 1.1
    adjust_to_optimal_speed()
    assert g.outspeedcm == 20
    g.can_ultra = -200
    adjust_to_optimal_speed()
    assert g.outspeed == 0

test_optimal_speed()
test_sensor_filter()
test_speed_control()
