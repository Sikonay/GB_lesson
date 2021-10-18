from itertools import zip_longest
import json

with open('users.csv', 'r', encoding='utf-8') as name, \
        open('hobby.csv', 'r', encoding='utf-8') as hobby:
    names = name.read().splitlines()
    hobbys = hobby.read().splitlines()

if len(names) < (hobbys):
    print(1)
else:
    user_hobby = dict(zip_longest(names, hobbys, fillvalue=None))
    with open('result_3.txt', 'w') as f:
        json.dump(user_hobby, f, ensure_ascii=False)
