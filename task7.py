""""

Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
 со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

"""

import json
profit_list = {}
format_list = {}
result = 0
result_out = 0
i = 0
fs = open('task7.txt', 'r', encoding="utf-8")
for line in fs:
    name, firm, earning, damage = line.split()
    profit_list[name] = int(earning) - int(damage)
    if profit_list.setdefault(name) >= 0:
       result = result + profit_list.setdefault(name)
       i += 1
       if i != 0:
          result_out = result / i
          print(f'Прибыль средняя - {result_out:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    format_list = {'средняя прибыль': round(result_out)}
    profit_list.update(format_list)
    print(f'Прибыль каждой компании - {profit_list}')

fs = open('task7.json', 'w', encoding="utf-8")
json.dump(profit_list, fs)
js_str = json.dumps(profit_list)
print(f'Создан файл с расширением json со следующим содержимым: \n '
      f' {js_str}')