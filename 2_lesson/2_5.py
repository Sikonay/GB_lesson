origin_list = [57.8, 46.51, 97, 59.5, 408, 502, 4540]
print(origin_list)
print(id(origin_list))

for i in range(len(origin_list)):
    numb_str = str("%.2f" % origin_list[i])
    print(f"{numb_str[:numb_str.find('.')]} руб {numb_str[numb_str.find('.')+1:]} коп", end=', ')

#сортировка по возрастанию
print()
origin_list.sort()
print(origin_list)
print(id(origin_list))

#По обыванию новом списке
new_list = sorted(origin_list, reverse=True)
print(new_list)

#5 дорогих товаров
print(sorted(origin_list, reverse=True)[:5])