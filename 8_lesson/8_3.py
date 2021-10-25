def type_logger(func):
    def wrapper(num):
        result = func(num)
        print(f'{num}: {type(num)}')
    return wrapper
@type_logger
def calc_cube(x):
    return x **3

a = calc_cube(5)