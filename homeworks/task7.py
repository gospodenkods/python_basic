""""

Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
(комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата


"""


class Complex:
    def __init__(self, var1, var2, *args):
        self.first = var1
        self.next = var2
        self.result = 'x + y * z'

    def __add__(self, in_other):
        print(f'Сумм арезультатов')
        return f'Result = {self.first + in_other.first} + {self.next + in_other.next} '

    def __mul__(self, other):
        print(f'Произведение результатов')
        return f'Result = {self.first * other.first - (self.next * other.next)} + {self.next * other.first} '

    def __str__(self):
        return f'Result = {self.first} + {self.next} '


print(Complex(5, -6))
print(Complex(9, 12))
print(Complex(5, -6) * Complex(9, 12))
