import os
folders = []

with open('config.yaml','r', encoding='utf-8') as f:
    for line in f:
        print(line.find(' '))
        print(line)
            #print(line[line.find('|--')+3:])

for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)