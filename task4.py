""""

Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Выполните вызов методов и также покажите результат.

Вообще  конечно , загнали по условиям  в жесткие рамки..  хоть чутка  разбавить юмором серые будни описания классов
и методов


"""

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name} Протяжка, продувка , ключ на "старт", помчались '

    def stop(self):
        return f'{self.name} стопЭ'

    #True на право False лево

    def turn(self, direction):
        if direction:
            return f'{self.name} на право '
        else:
            return f'{self.name}  на лево'

    def show_speed(self):
        return f'Текущая скорость коляски {self.name} составляет  {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая сокрость коляски {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Нарушаем {self.name} мчимся слишком быстро'
        else:
            return f'Ползем {self.name}  Собянин штраф не выпишит'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая спидуха  {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Нарушаем  {self.name} мчимся слишком быстро'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name}  тачила понтов'
        else:
            return f'{self.name}  норм коляска '


woodlet = SportCar(100, 'Желтенькая', 'Дроволет', False)
kamaz = TownCar(30, 'Рыжая', 'Космич', False)
lada_sedan_eggplant = WorkCar(70, 'Черненькая', 'Шайтан машина', True)
uncle_sem = PoliceCar(110, 'Blue', 'Дядя Сэм', True)
print(lada_sedan_eggplant.turn(True))
print(f'Когда  {kamaz.turn(False)}, Тогда {woodlet.stop()}')
print(f'{lada_sedan_eggplant.go()}  мчит быстро со скоростью  {lada_sedan_eggplant.show_speed()}')
print(f'{lada_sedan_eggplant.name} следующего цвета  {lada_sedan_eggplant.color}')
print(f'{woodlet.name} машина понтов ? {woodlet.is_police}')
print(f'{lada_sedan_eggplant.name}  машина понтов? {lada_sedan_eggplant.is_police}')
print(woodlet.show_speed())
print(kamaz.show_speed())
print(uncle_sem.police())
print(uncle_sem.show_speed())