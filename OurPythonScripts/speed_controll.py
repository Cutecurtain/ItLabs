from nav import g
from sensor_logic import get_filtered_sensor_value
from distance_logic import optimal_speed, optimal_distance

def adjust_to_optimal_speed():
    
    #in cm
    current_distance = get_filtered_sensor_value()
    
    # g.speed?? probably not right
    #new_distance = optimal_distance(g.speed)

    if current_distance != None:
        new_speed = optimal_speed(current_distance)
        if -30 < new_speed < 0:
            new_speed = -30
        elif 0 < new_speed < 30:
            new_speed = 30
    else:
        new_speed = 0

    
    g.outspeedcm = new_speed
        
from time import sleep
def keep_optimal_speed():
    while True:
        adjust_to_optimal_speed()
        sleep(0.1)
        
