for i in range(1,101):
    if i == 11 or i == 12 or i == 13 or i == 14:
        print(f'{i} процентов')
    elif i%10 == 1:
        print(f'{i} процент')
    elif i%10 == 2 or i%10 == 3 or i%10 == 4:
        print(f'{i} процентa')
    else:
        print(f'{i} процентов')