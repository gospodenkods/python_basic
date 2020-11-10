""""

Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

"""


def result_sum(file_for_open):
    fs = open(file_for_open, 'w+', encoding="utf-8")
    input_line = input('Введите цифры через пробел \n')
    fs.writelines(input_line)
    numbers = input_line.split()
    return sum(map(int, numbers))


print(f'Результатом работы является \n {result_sum("task5_number_list.txt")}')
