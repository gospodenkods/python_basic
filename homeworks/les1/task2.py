""""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

input_sec = int(input("Введите время в секундах!\n"))
hour = input_sec//3600
minute = (input_sec//60) % 60
second = input_sec % 60

if hour < 10:
    hour = str('0' + str(hour))
else:
    minute = str(minute)

if minute < 10:
    minute = str('0' + str(minute))
else:
    minute = str(minute)
if second < 10:
    second = str('0' + str(second))
else:
    second = str(second)

summary_string = f'Результатом проебразованиея секунд вво время: {hour}:{minute}:{second}'
print(summary_string)
