

input_num = input("Введите число \n")

while not input_num.isdigit():
    print("Вы ввели строку,а необходимо число \n")
    input_num = input("Введите число для сложения по алгоритму  n+nn+nnn=sum\n")

max_int = 0
for i in input_num:
    if int(i) > max_int:
        max_int = int(i)
print("Максимальное циффра в введенном числе:", max_int)


"""

Вообще все выше описанное мне не нравится , правильнее на мой взгляд так 
особо не проверял, так кинул мысли в коммент

input_num = list(map(int, input("Введите число \n").split()))

print max("Максимальное циффра в введенном числе:",list)


"""