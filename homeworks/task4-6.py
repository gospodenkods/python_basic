""""

Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

"""


def inputs(message):
    value = input(message + "\n")
    var_rig = is_digit(value)
    while not var_rig:
        print("Вы ввели строку,а необходимо число \n")
        value = input(message)
        var_rig = is_digit(value)
    return int(value)


def is_digit(string):
    if string.isdigit():
        return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


class Mashines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.number = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Наименование': self.name, 'Цена': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        name = input(f'Введите наименование ')
        price = inputs(f'Введите цену ')
        quanta = inputs(f'Введите количество ')
        update_string = {'Модель устройства': name, 'Цена за ед': price, 'Количество': quanta}
        self.my_unit.update(update_string)
        self.my_store.append(self.my_unit)
        print(f'Список -\n {self.my_store}')
        answer = input(f'Для выхода - E, продолжение - любую клавишу \n')

        if answer.lower() == 'e':
            self.my_store_full.append(self.my_store)
            return f'Склад -\n {self.my_store_full}'
        else:
            return Mashines.reception(self)



class Printer(Mashines):
    def to_print(self):
        return f'to print smth {self.number} times'


class Scanner(Mashines):
    def to_scan(self):
        return f'to scan smth {self.number} times'


class Copier(Mashines):
    def to_copier(self):
        return f'to copier smth  {self.number} times'


unit_1 = Printer('Iskra ES1018', 5000, 7, 10)
unit_2 = Scanner('Phaser', 2000, 10, 18)
unit_3 = Copier('Canon', 1800, 2, 35)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
