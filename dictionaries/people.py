person_0 = {
    'first': 'léa',
    'last': 'seydoux',
    'age': 38,
    'city': 'paris',
}
person_1 = {
    'first': 'margot',
    'last': 'robbie',
    'age': 33,
    'city': 'gold coast',
}
person_2 = {
    'first': 'rosamund',
    'last': 'pike',
    'age': 45,
    'city': 'london',
}

people = [person_0, person_1, person_2]

for person in people:
    print(f'Full name: {person['first'].title()} {person['last'].title()}\n'
          f'Age: {person['age']}\n'
          f'City: {person['city'].title()}\n')
    
