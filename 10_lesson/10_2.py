import abc

class Clothing(abc.ABC):
    def __init__(self, param):
        self.param = param

    @abc.abstractmethod
    def consumption(self):
        pass
class Coat(Clothing):
    @property
    def consumption(self):
        return self.param / 6.5 + 0.5
class Suit(Clothing):
    @property
    def consumption(self):
        return self.param * 2 + 0.3
obj1 = Coat(48)
obj2 = Suit(75)

print(obj1.consumption)
print(obj2.consumption)