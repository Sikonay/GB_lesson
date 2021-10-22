import re


def reg_parse(adres):
    print(re.split(r' ', adres)[0])
    print(adres)
    print(re.search(r'[.*]', adres).group())
    # print(re.split(r' ', adres)[3][1:])


with open('../8_lesson/nginx_logs.txt', 'r', encoding="utf-8") as f:
    my_list = [reg_parse(line) for line in f]

# print(my_list)
