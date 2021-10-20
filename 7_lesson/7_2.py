import os

blank = {}

with open('config.yaml', 'r', encoding='utf-8') as f:
    blank = dict(map(str.split, f.readlines()))

project_dir = blank.pop('base')
os.makedirs(project_dir, exist_ok=True)
os.chdir(project_dir)

for folder, files in blank.items():
    os.makedirs(folder, exist_ok=True)
    for file in files.split(','):
        with open(folder+'/'+file,'w') as f:
            print('файл создан')

print(blank)
