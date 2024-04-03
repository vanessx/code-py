glossary = {
    'dictionary': '{}',
    'lists': '[]',
    'tuples': '()',
    'function': 'abc()',
    'method': 'abc.()',
}
# adicionar mais key-value pairs
glossary['if'] = 'conditional'
glossary['for'] = 'loop'
# loop usando o método keys() para retornar as keys e values
for word, meaning in glossary.items():
    print(f'Python materialise {word.title()} like this {meaning}\n')

print(glossary)
