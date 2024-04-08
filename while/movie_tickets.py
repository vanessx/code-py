while True:
    age = input('How old are you? \n'
                'Type quit to exit.\n')
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print('Your ticket is free.')
    elif age <= 12:
        print('Your ticket costs 10€.')
    elif age > 12:
        print('Your ticket costs 15€.')