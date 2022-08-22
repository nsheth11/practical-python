import time

def timed(func):
    def wrapper(*pargs, **kwargs):
        start = time.time()
        r = func(*pargs, **kwargs)
        end = time.time()
        print('%s.%s: %f' % (func.__module__, func.__name__, end-start))
        return r
    
    return wrapper