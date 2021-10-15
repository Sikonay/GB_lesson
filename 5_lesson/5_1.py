def odd_nums(num):
    for numb in range(1, n + 1, 2):
        yield numb


odd_to = odd_nums(10)
print(next(odd_to))
print(next(odd_to))
print(odd_to)
