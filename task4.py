""""
Со словарем еще  воевать



"""

translate_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четырка'}
my_list = []
result = []

fs = open("translate_number.txt", 'r', encoding="utf-8")
for line in fs:
    split_list = line.split(" - ")
    print(split_list)
    if split_list[0] in translate_dict:
        word_list = translate_dict[split_list[0]]
        result.append(word_list + ' - ' + split_list[1])
print(result)

file_output = open("translate_number_new.txt", "w", encoding="utf-8")
file_output.writelines(result)
file_output.close()
