import re


def reg_parse(adres):

    # print(re.split(r' ', adres)[0])                     #   ip
    # print(re.search(r'\[(.*?)\]', adres).group()[1:-1])       #   data
    # print(re.search(r'([A-Z]{3})', adres).group())      #   GET
    # print(re.search(r'\s(\/[\w\/]+)', adres).group()[1:])   #   path
    # print(re.search(r'\s(\d{3})\s', adres).group()[1:])     #
    # print(re.search(r'\d+ "', adres).group()[:-2])

    remote_addr = re.split(r' ', adres)[0]
    request_datetime = re.search(r'([A-Z]{3})', adres).group()
    request_type = re.search(r'([A-Z]{3})', adres).group()
    requested_resource = re.search(r'\s(\/[\w\/]+)', adres).group()[1:]
    response_code = re.search(r'\s(\d{3})\s', adres).group()[1:]
    response_size = re.search(r'\d+ "', adres).group()[:-2]

    return (remote_addr,request_datetime, request_type, requested_resource, response_code, response_size)



with open('../8_lesson/nginx_logs.txt', 'r', encoding="utf-8") as f:
    my_list = [reg_parse(line) for line in f]

for list_m in my_list:
    print(list_m)