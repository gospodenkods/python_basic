"""

Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

"""


def to_int(inputs):
    buffer = ""
    for char in inputs:
        if char.isdigit():
            buffer += char
    if buffer.isdigit():
        return int(buffer)
    else:
        return 0


subject_list = {}
fs = open('subject_file.txt', 'r', encoding="utf-8")
for line in fs:
    sub_h, lec_h, prac_h, lab_h = line.split()
    subject_list[sub_h] = to_int(lec_h) + to_int(prac_h) + to_int(lab_h)
print(f'Общее количество часов по предмету - \n {subject_list}')
