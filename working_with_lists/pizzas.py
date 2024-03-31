pizzas = ['neapolitan', 'greek', 'margherita', 'portuguese', 'new york']
friend_pizzas = pizzas[:] # copia a lista pizzas

# adicionar um tipo de pizza
pizzas.append('sicilian')
friend_pizzas.append('roman')

print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizza are:")
for pizza in friend_pizzas:
    print(pizza.title())
