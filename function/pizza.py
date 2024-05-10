# usamos * quando não sabemos o número exato de argumentos que a função usará
def make_pizza(*toppings):
    print('Making a pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')