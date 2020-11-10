""""

Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников

Попса, похулиганил ,ввел тригер  на сумму оклада

"""


def inputs(message):
    value = input(message + "\n")
    while not value.isdigit():
        print("Вы ввели строку,а необходимо число \n")
        value = input(message)
    return int(value)


trigger = inputs("Введите условия отбора по окладу ")

fs = open('salary_file.txt', "r", encoding="utf-8")
salaries_list = []
lees_list = []
read_list = fs.read().split('\n')
for i in read_list:
    i = i.split()
    if int(i[1]) < trigger:
        lees_list.append(i[0])
    salaries_list.append(i[1])
print(f'Оклад меньше {trigger} {lees_list}, средний оклад {sum(map(int, salaries_list)) / len(salaries_list)}')
