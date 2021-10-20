import os
import json

strukt = {}

for roots, dirs, files in os.walk('my_project'):
    for file in files:
        format_10 = os.stat(os.path.join(roots, file)).st_size // 10 * 10 + 14
        name = file.rsplit('.')[-1]
        if format_10 in strukt:
            strukt[format_10][1].append(name)
            strukt[format_10] = (strukt[format_10][0]+1, list(set(strukt[format_10][1])))
        else:
            strukt.setdefault(format_10,(1,[name]))

res_d = {k: strukt[k] for k in sorted(strukt.keys())}

with open('result.json','w') as f:
    json.dump(res_d,f)

with open('result.json','r') as f:
    print(json.load(f))

