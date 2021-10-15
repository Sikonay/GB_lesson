odd_to = int(input('Введите номер '))

result = (numb for numb in range(1, odd_to + 1, 2))

print(next(result))
print(next(result))
print(list(result))
