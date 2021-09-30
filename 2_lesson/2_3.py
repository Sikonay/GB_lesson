my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print(my_list)
print(id(my_list))

i = 0 #счетчик для цикла и индекс списка

while i < len(my_list):
    #if len(my_list[i]) == 1 and my_list[i].isdigit():
    #    my_list[i] = '0' + my_list[i]

    if my_list[i].isdigit() or my_list[i][1:].isdigit():
        if len(my_list[i]) == 1:
            my_list[i] = '0' + my_list[i]
        if my_list[i][0] == '-' or my_list[i][0] == '+':
            my_list[i] = my_list[i][0]+'0'+my_list[i][1:]

        my_list.insert(i, '"')
        my_list.insert(i + 2, '"')
        i += 1
    i += 1

# вывод строки
#stroka = " ".join(my_list)
stroka = ''
for i in range(len(my_list)):
    if my_list[i].isdigit() or my_list[i][1:].isdigit() or my_list[i] == '"':
        stroka += my_list[i]
    elif i <len(my_list)-1:
        if (my_list[i+1].isdigit() or my_list[i+1][1:].isdigit() or my_list[i+1] == '"'):
            stroka += ' ' + my_list[i] + ' '
        else:
            stroka += ' ' + my_list[i]
    else:
        stroka += ' ' + my_list[i]

print(my_list)
print(id(my_list))
print(stroka.strip())