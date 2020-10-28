
input_num = int(input("Введите число \n"))
"""
while not input_num.isdigit():
    print("Вы ввели строку,а необходимо число \n")
    input_num = input("Введите число для сложения по алгоритму  n+nn+nnn=sum\n")

max_int = 0
for i in input_num:
    if int(i) > max_int:
        max_int = int(i)
print("Максимальное циффра в введенном числе:", max_int )
"""


division = input_num % 10
input_num = input_num//10
while input_num > 0:
    if input_num % 10 > division:
        division = input_num % 10
    input_num = input_num//10

print("Максимальное циффра в введенном числе:", division)