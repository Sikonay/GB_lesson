# class Auto:
#     # Атрибуты
#     auto_name = 'Mercedes'
#     auto_model = 'S600'
#     auto_year = 2021
#
#     # методы класса
#     def on_auto_start(self):
#         print(f'Заводим автомобился')
#
#     def on_auto_stop(self):
#         print('Стоп работу двигателя')
#
#
# a = Auto()
# b = Auto()
# print(a)
# print(type(a))
#
# print(a.auto_name, a.auto_model)
#
# a.on_auto_start()
# a.on_auto_stop()
#
# class Auto:
#     # Атрибуты
#     auto_count = 0
#
#     # методы
#     def on_auto_start(self, auto_name, auto_model, auto_year):
#         print("автомобиль зведен")
#         self.auto_name = auto_name
#         self.auto_model = auto_model
#         self.auto_year = auto_year
#         Auto.auto_count += 1
#
#
# a = Auto()
# a.on_auto_start('Lexus', 'RX 350', 2019)
# print(a.auto_name,a.auto_count)
# a.on_auto_start('Lexus', 'RX 350', 2019)
# print(a.auto_name,a.auto_count)
# a.on_auto_start('Lexus', 'RX 350', 2019)
# print(a.auto_name,a.auto_count)

# class Auto:
#     #Атрибуты
#     auto_count = 0
#
#     def __init__(self,asd='None'):
#         self.auto_name =asd
#         Auto.auto_count +=1
#         print(Auto.auto_count,self.auto_name)
#
# a = Auto()
# a = Auto('Mercedes')
# b = Auto('BMW')
# c = Auto('Lexus')

class Auto:
    def __init__(self):
        print('Автомобиль зведен')
        self.auto_name = 'Mazda'
        self._auto_model = 'CX9'
        self.__auto_year = 2019

a = Auto()
print(a.auto_name)
print(a._auto_model)