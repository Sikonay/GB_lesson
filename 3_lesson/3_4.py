def thesaurus(*args):
    result = {}
    for name in args:
        if result.get(name[0][0]):
            result[name[0][0]].append(name)
        else:
            result[name[0][0]] = [name]
    return (result)

def thesaurus_adv(*args):
    result = {}
    for name in args:
        sur_name = name.split()[1][0]

        if result.get(sur_name):
            result[sur_name].append(name)
        else:
            result[sur_name] = [name]
    for item in result:
        result[item] = thesaurus(*result[item])
    return result

print(thesaurus("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))