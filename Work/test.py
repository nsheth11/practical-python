'test.py'
from timethis import timed

def logged(func):
    def wrapper(*arg, **kwarg):
        print(f'Calling {func.__name__}')
        return func(*arg, **kwarg)
    return wrapper

@logged
def add(a, b):
    return a + b
@timed
def countdown(n):
     while n > 0:
         n-=1