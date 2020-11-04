""""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

"""

def m_fn(input_name='Иван', input_lastname='Иванов', input_age='144', input_city='Колыма',
         input_mail='директор_мира@mail.ru', input_mobile='8-000-000-00-00'):
    return ' '.join([input_name, input_lastname, input_age, input_city, input_mail, input_mobile])


input_name = input('Ваше имя?')
input_lastname = input('Ваша фамилия?')
input_age = input('Признавайтесь.Сколько вам лет ?')
input_city = input('Ваш г...д  герой?')
input_mail = input('а теперь ваше мыло.Ну..  e-mail ?')
input_mobile = input('Укажи цифры , звякну на мобилку !?')

print(m_fn(input_name, input_lastname, input_age, input_city,
           input_mail, input_mobile))
