""""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
 Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите
 численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника .

"""

def inputs(message):
    value = input(message+"\n")
    while not value.isdigit():
        print("Вы ввели строку,а необходимо число \n")
        value = input(message)
    return int(value)


input_revenue = inputs("Введите значение выручки")

input_costs = inputs("Введите значение издержек")

if input_revenue-input_costs > 0:
    result_string = f"У вас прибыльный бизнес и его прибыль составляет: {input_revenue-input_costs} рябчиков\n"
    print(result_string)
    profitability = f"Рентабельность составляет: {((input_revenue-input_costs)/input_revenue)*100}%\n"
    print(profitability)
    member_count = inputs("Введите числинность сотрудников")
    for_one_member = f"Прибыль на одного сотрудника составляет {(input_revenue-input_costs)/member_count} рябчиков"
    print(for_one_member)
else:
    print("У вас убыточный бизнес и его убыток составляет: ", (input_revenue - input_costs)*-1)


#print(input_revenue)

#    input("Введите значение выручки \n")

#input_costs = input("Введите значение излержек \n")


