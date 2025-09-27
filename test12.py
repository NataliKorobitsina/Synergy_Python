# Урок № 15, задание 1
class Transport(object):
    def __init__(self, name, max_speed, mileage):
       self.name=name
       self.max_speed=max_speed
       self.mileage=mileage

    def info(self):
        print(f'Название автомобиля {self.name}. Скорость {self.max_speed}. Пробег {self.mileage}')

Autobus=Transport('Renault Logan', 180, 12)
Autobus.info()


# Урок № 15, задание 2
class Transport:

    def __init__(self, name, max_speed, mileage):
       self.name=name
       self.max_speed=max_speed
       self.mileage=mileage

    def seating_capacity(self, capacity):
        return f'Вместимость {self.name} {capacity} пассажиров'

class Autobus(Transport):

    def seating_capacity(self, capacity=50):
        return f'Вместимость одного автобуса {self.name} {capacity} пассажиров'

my_bus=Autobus('Renault Logan', 180, 12)
print(my_bus.seating_capacity())
