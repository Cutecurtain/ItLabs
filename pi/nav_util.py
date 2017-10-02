def dist(x1, y1, x2, y2):
    from math import sqrt
    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def sign(x):
    if x == 0:
        return 0
    else:
        from math import copysign
        return int(copysign(1, x))

def start_new_thread(f, args):
    from sys import version_info
    from threading import Thread
    if version_info < (3,):
        thread = Thread(target=f, args=args)
    else:
        thread = Thread(target=f, args=args, daemon=True)
    thread.start()
    return thread

rev = reversed
min = min
