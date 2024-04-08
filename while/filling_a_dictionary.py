responses = {}
# usamos uma flag para indicar que a sondagem está ativa
polling_active = True

while polling_active:
    name = input('What is your name? ')
    response = input('Which mountain would you like to climb someday? ')
    
    # guardar a resposta no dicionário
    responses[name] = response

    # saber se mais alguém vai participar na sondagem
    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        polling_active = False

print('----- Poll results -----')
for name, response in responses.items():
    print(f'{name} would like to climb {response}')