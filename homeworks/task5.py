"""

Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом
и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо
числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен после
нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и
после этого завершить программу


"""


def dgt(input_num):
    while not input_num.isdigit():
        print("Вы ввели строку,а необходимо число \n")
        input_num = input("Введите число для сложения\n")
    return int(input_num)


def my_sum():
    result_sum = 0
    trigger = False
    while not trigger:
        input_number = input('Для выхода жмякаем Q- \n').split()

        var_trigger = 0
        for i in range(len(input_number)):
            if input_number[i].lower() == 'q':
                trigger = True
                break
            else:
                var_trigger = var_trigger + dgt(input_number[i])
        result_sum = result_sum + var_trigger
        print(f'Смежный результат {result_sum}')
    print(f'Итоговый результат {result_sum}')


my_sum()
