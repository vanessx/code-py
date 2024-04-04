# lista dentro de um dicionário
favorite_places = {
    'nathalie': ['porto', 'rome', 'paris'],
    'margot': ['madeira', 'toscana', 'stockholm'],
    'rosamund': ['shanghai', 'bangkok', 'rio de janeiro'],
}

for person, places in favorite_places.items():
    print(f'\n{person.title()} favorite places are:')
    for place in places:
        print(f'\t- {place.title()}')