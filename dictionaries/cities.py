cities = {
    'porto': {
        'country': 'portugal',
        'population': 214_349,
        'fact': 'one of the oldest cities in Europe',
    },
    'los angeles': {
        'country': 'united states of america',
        'population': 3_822_621,
        'fact': 'is the only North American city to have hosted the'
        'Olympics twice',
    },
    'paris': {
        'country': 'france',
        'population': 2_161_732,
        'fact': '"paris" is not the original name of the city'
    },
}

for city, info in cities.items():
    print(f'\nThree things about {city.title()}:')
    for key, value in info.items():
        print(f'\t{key}: {value}')
