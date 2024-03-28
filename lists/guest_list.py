guests = ['Margot', 'Rosamund', 'Tom', 'Paul']
print(len(guests))

print(f'Hi {guests[0]}, I am waiting for you.')
print(f'{guests[1]}, dinner is ready!')
print(f'Where is {guests[2]} and {guests[3]}?')

print(f'{guests[3]} can not come.')

guests[3] = 'Sydney' # trocar de convidado

print(f'Hi {guests[0]}, I am waiting for you.')
print(f'{guests[1]}, dinner is ready!')
print(f'Where is {guests[2]} and {guests[3]}?')

print('I found a bigger dinner table, I will invite a few more people.')

# adicionar mais convidados
guests.insert(0, 'Anya')
guests.insert(3, 'Jacob')
guests.append('Zendaya')

# remover alguns convidados
print(f'\n The table will not arrive in time so I will just invite two people.')
print(guests)

# depois que o primeiro é removido todas as posições mudam, daí ter muitos pop(2)
remove_guests = guests.pop(0), guests.pop(2), guests.pop(2), guests.pop(2), guests.pop(2)

print(f'Sorry {remove_guests} :( See you next time.')

print(f"Let's dinner, {guests[0]} and {guests[1]}!")

# remover todos os itens da lista
del guests[0]
del guests[0] # depois do primeiro removido, o segundo tem como posição 0

print(guests)

