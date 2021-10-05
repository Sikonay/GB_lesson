def thesaurus(*args):
    names = {}
    for i in range(len(args)):
        key_for = args[i][0]
        names[key_for] = list(filter(lambda x: x[0] == key_for, args))
    return names


def thesaurus_adv(*args):
    names = {}

    for i in range(len(args)):
        # print(i)
        key_name = str(args[i][0])
        # print(key_name)
        key_surname = str(args[i].split(' ')[1])[0]
        # key_surname = args[i].split(' ')[1]

        print(list(filter(lambda x: str(x.split(' ')[1])[0] == key_surname, args)))

        names[key_surname] = thesaurus(list(filter(lambda x: str(x.split(' ')[1])[0] == key_surname, args)))

        #names[key_surname] = thesaurus('Иван Сергеев', 'Инна Серова', 'Анна Савельева')

        print(key_name + ' / ' + key_surname)
    return names


print(thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева'))
print()
print(thesaurus('Иван Сергеев', 'Инна Серова', 'Петр Алексеев', 'Илья Иванов', 'Анна Савельева'))


t = {
        'С': {
            'Иван Сергеев': [['Иван Сергеев', 'Инна Серова', 'Анна Савельева']]
            },
        'А': {
            'Петр Алексеев': [['Петр Алексеев']]
            },
        'И': {
            'Илья Иванов': [['Илья Иванов']]
            }
    }