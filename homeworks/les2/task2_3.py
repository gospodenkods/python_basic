"""Пользователь вводит месяц в виде целого числа от 1 до 12.Сообщить к какому времени года относится месяц (зима, весна,
лето, осень).Напишите решения через list и через dict.
"""


# Немного рекурсии

def month_input():
    input_variable = input("Введите номер месяца от 1-12\n")

    if not input_variable.isdigit():
        print("Вы ввели строку необходимо число\n")
        input_variable = month_input()
    return int(input_variable)


seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
seasons_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
month = month_input()

while month > 12:
    print('Сорри но вы ввели недействительный номер месяцат\n Ведите от 1-12')
    month = month_input()

if month == 1 or month == 12 or month == 2:
    print("Решение dict ", seasons_dict.get(1))
    print("Решение list ", seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print("Решение dict ", seasons_dict.get(2))
    print("Решение list ", seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print("Решение dict ", seasons_dict.get(3))
    print("Решение list ", seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print("Решение dict ", seasons_dict.get(4))
    print("Решение list ", seasons_list[3])
