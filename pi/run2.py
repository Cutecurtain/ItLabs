import nav as n
import time
import speed_controll as sc
from nav import *
from nav1 import whole4, pause, cont
from driving import stop, drive, steer
import car_driver as cd
init()
g.speedlimit = None
g.outspeedcm = 0

sc.keep_optimal_speed()
