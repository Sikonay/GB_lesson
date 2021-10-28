class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name, self.is_police = speed, color, name, is_police

    def go(self):
        print(f"{self.color} {self.name} поехала")

    def stop(self):
        print(f"{self.color} {self.name} останавилась")

    def turn(self, direction):
        self.direction = direction
        print(f"{self.color} {self.name} повернул на {self.direction}")

    def show_speed(self):
        print(f"Скорость: {self.speed}")

    def check_police(self):
        print(f"Полицейская: {self.is_police}")

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f"Скорость: {self.speed}") if self.speed <= 60 else print("Превышена допустимая скорость")

    def check_police(self):
        print(self.is_police)

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class WorkCar(Car):
    def __init__(self,speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        print(f"Скорость: {self.speed}") if self.speed <= 40 else print("Превышена допустимая скорость")

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

    def check_police(self):
        print(f"Полицейская: {self.is_police}")

c, t, s, w, p = Car(40, "Белая", "Audi"), TownCar(40, "Черная", "BMW"), SportCar(40, "Красная", "Ferrari"),\
    WorkCar(40, "Вишневая", "Lada"), PoliceCar(40, "Серая", "Shkoda")

t.go(), t.turn("право"), t.stop()
t.show_speed(), t.check_police()

print(f"Марка: {t.name}, цвет: {t.color}, скорость: {t.speed}, Полицейская: {t.is_police} \n")