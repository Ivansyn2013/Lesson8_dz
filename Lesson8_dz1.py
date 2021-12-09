# Написать функцию email_parse(<email_address>), которая при
# помощи регулярного выражения извлекает имя пользователя и почтовый
# домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError. Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
#
import sys
import re


def email_parse(argv):
    print(sys.argv[1])
    result_dict = {}

    result_dict = {'username': re.split(r'[@\.]', sys.argv[1])[0], 'domain': re.split(r'[@\.]', sys.argv[1])[1]}

    print(result_dict)

    # print (re.split(r'[@\.]', sys.argv[1]) , re.search(r'@\w\.',sys.argv[1]))


email_parse(sys.argv[1])
