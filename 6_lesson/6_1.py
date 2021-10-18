with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    my_list = []
    for line in f:
        adr = line[:line.find(' ')]
        type = line[line.find('"') + 1:line.find('"') + 4]
        resurse = line[line.find('/d'):line.find('HTTP') - 1]
        requests = (adr, type, resurse)
        my_list.append(requests)
        print(requests)
