""""

Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат
вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()

"""
from functools import reduce


def result_fn(first_arg, next_arg):
    return first_arg * next_arg


print(f'Список чеиных чиселот 100 до 1000 {[element for element in range(99, 1001) if element % 2 == 0]}')
print(f'Результат произведения всех элементов списка \
       {reduce(result_fn, [i for i in range(99, 1001) if i % 2 == 0])}')
