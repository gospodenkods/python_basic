""""

Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

"""


class Textile:
    def __init__(self, var_width, var_height):
        self.width = var_width
        self.height = var_height

    def get_square(self, triger):
        if triger:
            return round(self.width / 6.5 + 0.5)
        else:
            return round(self.height * 2 + 0.3)

    @property
    def get_full_square(self):
        return str(f'S общая \n'
                   f' {(round(self.width / 6.5 + 0.5)) + (round(self.height * 2 + 0.3))}')


class Jacket(Textile):
    def __init__(self, var_width, var_height):
        super().__init__(var_width, var_height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'S костюм {self.square_j}'


class Coat(Textile):
    def __init__(self, var_width, var_height):
        super().__init__(var_width, var_height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'S пальто  {self.square_c}'


coat = Coat(3, 6)
jacket = Jacket(2, 7)
print(coat)
print(jacket)
print(f' пальто {coat.get_full_square}')
print(f' костюм {jacket.get_full_square}')
print(coat.get_square(True))
print(jacket.get_square(False))
