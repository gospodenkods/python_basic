"""

Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной
первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
буквы. Необходимо использовать написанную ранее функцию int_func()


"""


# Сама функция
def up_smb(a):
    word_list = a.split(' ')
    return_list = []
    for i in word_list:
        element = str(i)
        first_letter = element[:1].upper()
        word = first_letter + element[1:]
        return_list.append(word)
    return return_list


print(up_smb("hello world"))

# Тут  погоняем ее в цикле

trigger = False
while not trigger:
    input_string = input('Для выхода жмякаем Q- \n')
    if input_string.lower() == 'q':
        trigger = True
        break
    else:
        input_str = input("Введите строку \n ")
        print(up_smb(input_str))
