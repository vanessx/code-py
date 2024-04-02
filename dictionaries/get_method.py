favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f'Sarah favorite language is {language}.')

# usar o método get() para devolver um valor caso o pedido de keyvalue não existir
point_value = favorite_languages.get('points', 'No point value assigned.')
print(point_value)