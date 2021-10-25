import functools


def val_cheker(l_func):
    def _val_cheker(func):
        @functools.wraps(func)
        def wrapper(num):
            if l_func(num):
                print(func(num))
            else:
                raise ValueError(f'wrong value:{num}')

        return wrapper
    return _val_cheker

@val_cheker(lambda x: x > 0)
def calc_sube(x):
    return x ** 3

calc_sube(5)