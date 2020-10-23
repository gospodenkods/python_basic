"""
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
 и сохраните в переменные, выведите на экран.

"""
firs_variable = "Sunday"
next_variable = "Moscow"
last_variable = 10

print(firs_variable, 'Day of week')
print(next_variable, 'City where you live')
print(last_variable, 'Your favorite number')

firs_variable = input('What day is today?\n')
next_variable = input('What city do you live in?\n')
last_variable = input('What you favorite number?\n')

summary_line = f"Day of week '{firs_variable}' city where you live '{next_variable}' \
Your favorite number '{last_variable}'"

print(summary_line)
