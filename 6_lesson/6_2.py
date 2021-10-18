with open('nginx_logs.txt', 'r', encoding="utf-8") as f:
    my_list = [line[:line.find(' ')] for line in f]

adr = max(set(my_list), key=my_list.count)
print(adr, my_list.count(adr))



 #sdf