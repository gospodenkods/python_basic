""""

Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


"""


class Data:
    def __init__(self, day_month_year):

        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date_list = []

        for i in day_month_year.split():
            if i != '-': date_list.append(i)

        return int(date_list[0]), int(date_list[1]), int(date_list[2])

    @staticmethod
    def valid(day, month):

        if day in range(1, 31) and month in range(1, 12):
            return 'f  Даты валидные'
        else:
            return f'Ошибка!! Данные за пределами календаря'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('01 - 1 - 2020')
print(today)
print(Data.valid(10, 10))
print(today.valid(12, 14))
print(Data.extract('17 - 21 - 2055'))
print(today.extract('07 - 01 - 2098'))
print(Data.valid(8, 9))
