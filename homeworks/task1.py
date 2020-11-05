"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""


def inputs(message):
    value = input(message + "\n")
    while not value.isdigit():
        print("Вы ввели строку,а необходимо число \n")
        value = input(message)
    return int(value)


def prod_sale():
    trigger = False
    while not trigger:
        input_number = input('Для выхода жмякаем Q для  продолжения любую конопульку \n').split()
        for i in range(len(input_number)):
            if input_number[i].lower() == 'q':
                trigger = True
                break
            else:
                var_time = inputs('Выработка в часах?')
                var_salary = inputs('Ставка ?')
                var_bonus = inputs('Премия ?')
                result = var_time * var_salary + var_bonus
                print(f'Дядька заработал {result}')


prod_sale()
