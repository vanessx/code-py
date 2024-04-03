favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

friends = ['phil', 'sarah']
# loop por todas as keys usando o método keys()
for name in favorite_language.keys():
    print(f'Hi {name.title()}!')
    if name in friends:
        language = favorite_language[name].title()
        print(f'\t{name.title()}, I see you love {language}!')

if 'erin' not in favorite_language.keys():
    print('Erin, please take our poll!')

# sorted() printa em ordem alfabética
for name in sorted(favorite_language.keys()):
    print(f'\n{name.title()}, thank you for taking the poll.')
