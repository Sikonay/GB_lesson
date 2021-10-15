from itertools import zip_longest, islice

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена','Max', 'Bob'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

gen = ((tutors, klasses) for tutors, klasses in zip_longest(tutors, klasses, fillvalue=None))

print(*islice(gen, len(tutors)), sep='\n')
