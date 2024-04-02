# começar com um dicionário vazio
alien_0 = {}
# adicionar key-values ao dicionário
alien_0['color'] = 'green'
alien_0['points'] = '5'

print(alien_0)
print(f'The alien is {alien_0['color']}.')

# modificar um valor no dicionário
alien_0['color'] = 'yellow'
print(f'Now the alien is {alien_0['color']}.')

# remover key-value do dicionário (permanentemente)
del alien_0['points']
print(alien_0)