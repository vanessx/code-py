sandwich_orders = ['tuna sandwich', 'pastrami', 'chicken sandwich', 'pastrami',
                    'pastrami', 'pork sandwich', 'veggie sandwich']
finished_sandwiches = []

print('The Deli has run out of pastrami.')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
while sandwich_orders:
    current_order = sandwich_orders.pop().title()
    print(f'I am working on your {current_order}.')
    finished_sandwiches.append(current_order)

for finished_sandwich in finished_sandwiches:
    print(f'{finished_sandwich} is ready!')
