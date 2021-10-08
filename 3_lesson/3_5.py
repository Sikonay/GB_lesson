import random

def get_jokes(num, flag=False):
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    jokes = []
    my_list = min(no, adv, adj)
    while num and len(my_list):
        number = random.randrange(len(my_list))

        if flag:
            jokes.append(f'{no.pop(number)} {adv.pop(number)} {adj.pop(number)}')
        else:
            jokes.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
        num -=1
    return jokes

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(5))
