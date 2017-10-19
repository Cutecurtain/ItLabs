from nav import init, g
import car_driver as cd
print("running init")
init()
print("finished init")
g.limitspeed = None
print("limitspeed set")
print("running car_driver server")
cd.run()
print("finished")
