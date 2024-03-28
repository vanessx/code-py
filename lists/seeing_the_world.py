locations = ['los angeles', 'gold coast', 'stockholm', 'lagos', 'rome']
print(locations)

# modificar temporariamente a lista em ordem alfabética
print(sorted(locations))

# a lista mantêm-se original
print(locations)

# modificar temporariamente a lista em ordem alfabética contrária
print(sorted(locations, reverse=True))

# ainda original
print(locations)

# modificar permanentemente a lista em ordem contrária à original
locations.reverse()
print(locations)

# usar o mesmo método para a lista voltar à ordem original
locations.reverse()
print(locations)

# modificar permanentemente a lista em ordem alfabética
locations.sort()
print(locations)

# modificar permanentemente a lista em ordem alfabética contrária
locations.sort(reverse=True)
print(locations)