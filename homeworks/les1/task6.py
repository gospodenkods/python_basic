"""
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен
увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат
спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно
натуральное число — номер дня.
Например: a = 2, b = 3.


"""


def inputs(message):
    value = input(message + "\n")
    while not value.isdigit():
        print("Вы ввели строку,а необходимо число \n")
        value = input(message)
    return int(value)


def percent_in_day(value, percent_value):
    return value + (value / 100) * percent_value


input_first = inputs("Введите значение пробежки в первый день")

input_last = inputs("Введите значение требуемого киллометража")

trigger_day = 1
# sum =
while input_last > input_first:
    input_first =  percent_in_day(input_first, 10)
    trigger_day = trigger_day+1
  #  print(input_first)

print(f"На  день под номером  {trigger_day} ,спорстмен выполнил задуманное  ")
