import sys

users, hobby, combined = sys.argv[1:]

if __name__ == '__main__':
    from itertools import zip_longest

    with open(users, 'r', encoding='utf-8') as name, \
            open(hobby, 'r', encoding='utf-8') as hobby:
       names = name.read().splitlines()
       hobbys = hobby.read().splitlines()

    result = ((names, hobbys) for names, hobbys in zip_longest(names, hobbys, fillvalue=None))

    with open(combined, 'w') as f:
        for user in result:
            f.write(f'{user[0]}: {user[1]}\n')
    exit()
