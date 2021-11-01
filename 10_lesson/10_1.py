import itertools


class Matrix:
    def __init__(self, data):
        self.matrx = data

    def __str__(self):
        print(f'-' * (len(self.matrx[0]) * 6 + 1))
        for items in self.matrx:
            for item in items:
                print(f'| {item:^4d}', end='')
            print('|')
        return f'-' * (len(self.matrx[0]) * 6 + 1)
    def __add__(self, other):
        sum_matrix = []
        for items_self, items_other in itertools.zip_longest(self.matrx, other.matrx, fillvalue=0):
            result = list(map(lambda x:x[0] + x[1], itertools.zip_longest(items_self, items_other,fillvalue=0)))
            sum_matrix.append(result)
        return Matrix(sum_matrix)

