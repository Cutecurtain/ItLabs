import nav as n
import time
import speed_controll as sc
from nav import *
from nav1 import whole4, pause, cont
from driving import stop, drive, steer
import car_driver as cd
print("running init")
init()
print("finished init")
g.limitspeed = None
print("limitspeed set")
cd.run()
print("cd.run ran")
