person = {
    'first_name': 'léa',
    'last_name': 'seydoux',
    'age': 38,
    'city': 'paris',
}

first_name = person['first_name'].title()
last_name = person['last_name'].title()
age = person['age']
city = person['city'].title()

print(f'Her name is {first_name} {last_name}, she is {age} years old and lives in {city}.')
