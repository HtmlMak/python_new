class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
#        self.current_speed = current_speed

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self, current_speed):
        print(f'Машина едет со скоростью {current_speed} километров в час')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, current_speed):
        if current_speed > 60:
            print(f'Скорость {current_speed} киломметров в час превышает допустимую')
        else:
            print(f'Машина едет со скоростью {current_speed} километров в час')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self, current_speed):
        if current_speed > 40:
            print(f'Скорость {current_speed} киломметров в час превышает допустимую')
        else:
            print(f'Машина едет со скоростью {current_speed} километров в час')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

auto_1 = TownCar(180, 'black', 'KIA', False)
print(auto_1.speed)
print(auto_1.color)
print(auto_1.name)
print(auto_1.is_police)
auto_1.go()
auto_1.turn('налево')
auto_1.show_speed(80)
auto_1.show_speed(60)
auto_1.stop()

auto_2 = WorkCar(100, 'red', 'KAMAZ', False)
auto_2.show_speed(60)
auto_2.show_speed(40)

auto_3 = PoliceCar(200, 'grey', 'BMW', True)
print(auto_3.is_police)