unconfirmed_users = ['léa', 'paul', 'margot']
confirmed_users = []

while unconfirmed_users: # será executado o loop atá a lista estar vazia
    current_user = unconfirmed_users.pop() # remove o item da lista e atribui-o a uma variável
    print(f'Verifying user: {current_user.title()}.')
    confirmed_users.append(current_user) # adiciona à lista dos confirmados

print('The following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())