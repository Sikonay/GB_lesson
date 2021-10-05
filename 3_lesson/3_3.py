def thesaurus(*args):
    names = {}
    for i in range(len(args)):
        key_for = args[i][0]
        names[key_for] = list(filter(lambda x: x[0]== key_for, args))
    return names

print(thesaurus('asad', 'sfdg', 'sdf'))
