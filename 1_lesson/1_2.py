cube_list = []
for i in range(1, 1001, 2):
    cube_list.append(i ** 3)

result = 0

for i in range(len(cube_list)):
    division = cube_list[i]
    sum = 0

    while division > 0:
        sum = sum + (division % 10)
        division = division // 10

    if sum % 7 == 0:
        result = result + cube_list[i]

print(result)

# то же самое только +17
result = 0
for i in range(len(cube_list)):
    division = cube_list[i] + 17
    sum = 0

    while division > 0:
        sum = sum + (division % 10)
        division = division // 10

    if sum % 7 == 0:
        result = result + cube_list[i]
print(result)