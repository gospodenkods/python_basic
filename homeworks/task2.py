""""

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.


"""


class DivisionByZero:
    def __init__(self, var_x, var_y):
        self.divider = var_x
        self.denominator = var_y

    @staticmethod
    def divide_by_null(var_x, var_y):
        try:
            return var_x / var_y
        except:
            return f"Ошибка!!division by zero "


div = DivisionByZero(30, 200)
print(DivisionByZero.divide_by_null(10, 0))
print(DivisionByZero.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))
