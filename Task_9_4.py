from random import randrange, choice


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print(f'The car {self.name} is moving')

    def stop(self):
        print(f'The car {self.name} is stop')

    def turn(self):
        if randrange(0, 2) == 0:
            print('The car turn left')
        else:
            print('The car turn right')

    def show_speed(self):
        print(f'Current speed: {self.speed} km/h')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Over speed! Current speed: {self.speed} km/h')
        else:
            print(f'Current speed: {self.speed} km/h')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Over speed! Current speed: {self.speed} km/h')
        else:
            print(f'Current speed: {self.speed} km/h')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


color = ['red', 'green', 'white', 'black', 'yellow']
name = ['Audi', 'Lexus', 'Lada', 'KIA', 'BMW']
t = TownCar(randrange(0, 100), color[randrange(0, 5)], name[randrange(0, 5)], False)
t.go()
t.turn()
t.show_speed()
t.stop()
print(f'Color - {t.color}')
print(f'Police - {t.is_police}')
print('-' * 35)
w = WorkCar(randrange(0, 100), color[randrange(0, 5)], name[randrange(0, 5)], False)
w.go()
w.turn()
w.show_speed()
w.stop()
print(f'Color - {w.color}')
print(f'Police - {w.is_police}')
print('-' * 35)
s = SportCar(randrange(0, 100), color[randrange(0, 5)], name[randrange(0, 5)], False)
s.go()
s.turn()
s.show_speed()
s.stop()
print(f'Color - {s.color}')
print(f'Police - {s.is_police}')
print('-' * 35)
p = PoliceCar(randrange(0, 100), color[randrange(0, 5)], name[randrange(0, 5)], True)
p.go()
p.turn()
p.show_speed()
p.stop()
print(f'Color - {p.color}')
print(f'Police - {p.is_police}')
print('-' * 35)
