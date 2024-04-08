sandwich_orders = ['tuna sandwich', 'chicken sandwich', 'pork sandwich', 'veggie sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop().title()
    print(f'I am working on your {current_order}.')
    finished_sandwiches.append(current_order)

for finished_sandwich in finished_sandwiches:
    print(f'{finished_sandwich} is ready!')
