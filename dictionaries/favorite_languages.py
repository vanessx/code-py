favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people = ['peter', 'daniel', 'frances', 'jen', 'edward']

for person in people:
    if person in favorite_language.keys():
        print(f'{person.title()}, thank you for responding!')
    else:
        print(f'{person.title()}, you should take the poll!')