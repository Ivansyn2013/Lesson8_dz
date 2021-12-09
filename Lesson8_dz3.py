def tepy_loger(callback):
    def wrapper(*args):
        if len(args) == 1:
            print(f'{args[0]}:{type(args[0])}')
            print(callback(args[0]))
        else:
            for el in args:
                print(f'{el}:{type(args[0])} result {callback(el)}', end=',')

        return None

    return wrapper


@tepy_loger
def calc_cube(x):
    return x ** 3


print(calc_cube(5, 6, 7))
