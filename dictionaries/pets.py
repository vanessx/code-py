# lista vazia
pets = []
# dicionários que vão ser adicionados na lista
pet = {
    'breed': 'scottish fold',
    'owner': 'vanessa',
    'weight': 4.5,
    'eats': 'fish',
}
pets.append(pet)

pet = {
    'breed': 'bengal',
    'owner': 'léa',
    'weight': 4.1,
    'eats': 'chicken',
}
pets.append(pet)

pet = {
    'breed': 'ragdoll',
    'owner': 'paul',
    'weight': 5,
    'eats': 'snacks',
    }
pets.append(pet)

for pet in pets:
    print(f'Here is what I know about {pet['owner'].title()}:')
    for key, value in pet.items():
        print(f'\t{key}: {value}')