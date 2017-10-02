from nav import g
from sensor_logic import get_filtered_sensor_value
from distance_logic import optimal_speed, optimal_distance

def adjust_to_optimal_speed():
    
    #in cm
    current_distance = get_filtered_sensor_value()
    
    # g.speed?? probably not right
    #new_distance = optimal_distance(g.speed)
    
    new_speed = optimal_speed(current_distance)
    
    g.outputspeedcm = new_speed
        
from time import sleep
def keep_optimal_speed():
    while True:
        adjust_to_optimal_speed()
        sleep(0.1)
        
