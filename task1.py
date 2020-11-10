"""

Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.

"""

fs = open('test.txt', 'w', encoding="utf-8")
var_input = input('Введите текст ,для выхода нажмите Enter\n')
while var_input:
    fs.writelines(var_input)
    var_input = input('Введите текст ,для выхода нажмите Enter \n')
    if not var_input:
        break

fs.close()
fs = open('test.txt', "r", encoding="utf-8")
var_read = fs.readlines()
print(var_read)
fs.close()
