orig_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
print(orig_list)
print(id(orig_list))
for i in range(len(orig_list)):
    print(f"Привет, {orig_list[i][orig_list[i].rfind(' ') + 1:].title()}!")
    orig_list[i] = orig_list[i][:orig_list[i].rfind(' ') + 1].lower() + orig_list[i][orig_list[i].rfind(' ') + 1:].title()
print(orig_list)
print(id(orig_list))