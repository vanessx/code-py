# usamos * quando não sabemos o número exato de argumentos que a função usará
def make_pizza(size, *toppings):
    print(f'Making a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')