countries = ['portugal', 'australia', 'united states', 'italy', 'sweden']
print(countries)
print(countries[0].title()) # mostra o primeiro
print(countries[-1].title()) # mostra o último
print(len(countries)) # tamanho da lista

# usar valores individuais de uma lista
print(f'I am from {countries[0].title()} and I want to visit {countries[1].title()}.')

# mudar um valor de uma lista
countries[2] = 'united kingdom'
print(countries)

# adicionar um novo valor à lista
countries.append('iceland') # passa a ser o último valor da lista
print(f'\n{countries}')

# adicionar um novo valor a uma posição na lista
countries.insert(2, 'russia') # os outros valores passam a estar a um valor à direita
print(f'\n{countries}')

# remover um valor da lista
del countries[3]
print(f'\n{countries}')

# remover um valor da lista, mas ainda poder usá-lo
removed_country = countries.pop(2).title()
print(f'\n{countries}')
print(f'\nCountry removed: {removed_country}')

# remover um valor da lista se não soubermos o index e apenas o valor
too_cold = 'iceland'
countries.remove(too_cold)
print(f'\n{countries}')
print(f'\n{too_cold.title()} is too cold!')

# organizar permanentemente a lista em ordem alfabética
countries.sort()
print(f'\n{countries}')

# reverter a ordem da lista
countries.reverse()
print(f'\n{countries}')

# organizar temporariamente a lista em ordem alfabética
print(f'\n{sorted(countries)}')
