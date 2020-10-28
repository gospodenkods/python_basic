""""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
 Считаем 3 + 33 + 333 = 369 25.
"""

input_num = input("Введите число для сложения по алгоритму  n+nn+nnn=sum\n")

while not input_num.isdigit():
    print("Вы ввели строку,а необходимо число \n")
    input_num = input("Введите число для сложения по алгоритму  n+nn+nnn=sum\n")


result_nn = input_num+input_num

result_string = f"Результатом работы является {input_num}+{result_nn}+{input_num+result_nn}\n \
{int(input_num)+int(result_nn)+(int(input_num+result_nn))}"
print(result_string)



