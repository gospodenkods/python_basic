"""Реализовать структуру «Рейтинг», представляющую собой
не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться
после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде,
например, rating_list = [7, 5, 3, 3, 2].

Зациклим до выхода
Немного рекурсии для проверки на число :)
Ну нравится мне рекурсия
"""


def month_input():
    input_variable = input("Введите число (777 - выход)\n")

    if not input_variable.isdigit():
        print("Вы ввели строку необходимо число\n")
        input_variable = month_input()
    return int(input_variable)


rating_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {rating_list}")
input_digit = month_input()
while input_digit != 777:
    for el in range(len(rating_list)):
        if rating_list[el] == input_digit:
            rating_list.insert(el + 1, input_digit)
            break
        elif rating_list[0] < input_digit:
            rating_list.insert(0, input_digit)
        elif rating_list[-1] > input_digit:
            rating_list.append(input_digit)
        elif rating_list[el] > input_digit > rating_list[el + 1]:
            rating_list.insert(el + 1, input_digit)
    print(f"Текущий список  равен - {rating_list}\n")
    input_digit = month_input()
print("Работа програмульки завершена")
