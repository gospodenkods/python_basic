""""
 Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

"""

from itertools import count
from itertools import cycle


def inputs(message):
    value = input(message + "\n")
    while not value.isdigit():
        print("Вы ввели строку,а необходимо число \n")
        value = input(message)
    return int(value)


def count_fn(first, last):
    for element in count(first):
        if element > last:
            break
        else:
            print(element)


def cycle_fn(my_list, iterator):
    i = 0
    trigger = cycle(my_list)
    while i < iterator:
        print(next(trigger))
        i += 1


count_fn(first=inputs("С чего ведем отсчет ?"), last=inputs("Чем закончим?"))
cycle_fn(my_list=[1, 2], iterator=inputs("Значение итерации? "))
