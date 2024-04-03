rivers = {
    'nile': 'egypt',
    'amazon': 'brasil, peru and colombia',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print(f'The {river.title()} runs through {country.title()}.')

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())