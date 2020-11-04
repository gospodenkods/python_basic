"""

Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов

Не ну если my_func то  ок ,щя будет

"""


def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg2 < arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print(f'Результат - {my_func(int(input("First?")), int(input("Next?")), int(input("Last?")))}')
