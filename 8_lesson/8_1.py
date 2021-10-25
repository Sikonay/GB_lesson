import re


def email_parse(adres):
    try:
        return {'username': re.split(r'@',adres)[0], 'domain': re.split(r'@',adres)[1]}
    except :
        #print('Ошибка не смог разделить re.split')
        raise ValueError()

print(email_parse('kulumzhanov.s.b@gmail.com'))
