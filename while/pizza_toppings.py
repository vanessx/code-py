toppings = []

while True:
    topping = input('Enter a series of pizza toppings:'
                    '\nType \033[31mquit\033[m to exit.\n')
    if topping != 'quit':
        print(f'I will add {topping} to your pizza.')
        toppings.append(topping)
    else:
        break

print(f'Your toppings are: {toppings}')