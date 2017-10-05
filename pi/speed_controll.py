from nav import g
from sensor_logic import get_filtered_sensor_value
from distance_logic import optimal_speed

def adjust_to_optimal_speed():
    
    #in cm
    current_distance = get_filtered_sensor_value(0.1, 0.5)
    
    # g.speed?? probably not right
    #new_distance = optimal_distance(g.speed)
 
    new_speed = 0
    if current_distance != 0 and current_distance != 0.2:
        new_speed = optimal_speed(current_distance)
    print("current distance", current_distance)
    print("new speed", new_speed)
    print("")    
    g.outspeedcm = new_speed
        
from time import sleep
def keep_optimal_speed():
    while True:
        adjust_to_optimal_speed()
        sleep(0.1)
        
