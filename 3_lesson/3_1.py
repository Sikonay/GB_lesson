def repl(num):
    if num == 'zero':
        return 'ноль'
    elif num == 'one':
        return 'один'
    elif num == 'two':
        return 'два'
    elif num == 'three':
        return 'три'
    elif num == 'four':
        return 'четыре'
    elif num == 'five':
        return 'пять'
    elif num == 'six':
        return 'шесть'
    elif num == 'seven':
        return 'семь'
    elif num == 'eight':
        return 'восемь'
    elif num == 'nine':
        return 'девять'
    elif num == 'ten':
        return 'десять'
    else:
        print('введите на английском от 0 - 10')


def num_translate(num):

    if num == num.title():
        return repl(num.lower()).title()
    else:
        return repl(num.lower())


num = input('напишите число на англииском ')
print(num_translate(num))