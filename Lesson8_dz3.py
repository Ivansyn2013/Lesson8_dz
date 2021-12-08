def tepy_loger(callback):
    def wrapper(*args):
        print(*args, type(*args))
        return callback(*args)
    return wrapper

@tepy_loger
def calc_cube(x):
    return x**3



print(calc_cube(5))