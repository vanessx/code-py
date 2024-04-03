favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# loop por todos os valores usando o método values()
# se usarmos o método set() ele procura por valores duplicados e retorna o valor só uma única vez
print('The following languages have been mentioned:')
for language in set(favorite_language.values()):
    print(f'{language.title()}')