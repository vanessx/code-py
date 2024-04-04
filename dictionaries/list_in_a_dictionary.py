pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

print(f'Your order a {pizza['crust']}-crust pizza. '
      'With the following toppings:')

for topping in pizza['toppings']:
    print(f'\t- {topping}')