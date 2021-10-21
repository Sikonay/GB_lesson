import re


def email_parse(adres):
    return {'username': re.split(r'@',adres)[0], 'domain': re.split(r'@',adres)[1]}


print(email_parse('kulumzhanov.s.b@gmail.com'))
