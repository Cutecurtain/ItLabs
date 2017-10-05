import nav as n
from nav import *
from nav1 import whole4, pause, cont
from driving import stop, drive, steer
init()

loop = 100
a = 0
start = time.time()
for i in range(loop):
	a = g.can_ultra
	
end = time.time()
elapsed_time = end - start

print("readings per second")
print(loop/elapsed_time)

print("time per reading")
print(elapsed_time/loop) 	
