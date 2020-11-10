""""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.

"""

fs = open('test1.txt', "r", encoding="utf-8")
var_read = fs.read()
print(f'Прочтенное содержимое: \n {var_read}')
fs = open('test1.txt', "r")
var_read = fs.readlines()
print(f'Строк в файле - {len(var_read)}')

for i in range(len(var_read)):
    print(f'Символов {i + 1} - ой строки {len(var_read[i])}')
fs = open('test1.txt', 'r')
var_read = fs.read()
var_read = var_read.split()
print(f'Слов - {len(var_read)}')
fs.close()
