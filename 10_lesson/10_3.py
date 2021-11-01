class Cell:
    def __init__(self, wol):
        self.wol = wol
    def __add__(self, other):
        return self.wol + other.wol

    def __sub__(self, other):
        return self.wol - other.wol if self.wol - other.wol >= 0 else f'Разность меньше нуля'

    def __mul__(self, other):
        return Cell(self.wol * other.wol)

    def __floordiv__(self, other):
        return Cell(self.wol // other.wol)

    def __truediv__(self, other):
        return Cell(self.wol // other.wol)
    def make_order(self, n):
        for _ in range(self.wol // n):
            print('*' * n)
        print('*' * (self.wol % n))


a = Cell(12)
b = Cell(13)
c = Cell(5)

print(a + b)
