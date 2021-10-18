from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as name, \
        open('hobby.csv', 'r', encoding='utf-8') as hobby:
    names = name.read().splitlines()
    hobbys = hobby.read().splitlines()

result = ((names, hobbys) for names, hobbys in zip_longest(names, hobbys, fillvalue=None))

with open('result_4.txt', 'w') as f:
    for user in result:
        f.write(f'{user[0]}: {user[1]}\n')
