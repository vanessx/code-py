def formatted_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()

while True:
    print('Please tell me your name\n'
          '(enter \'q\' at any time to quit)')
    first = input('First name: ')
    if first == 'q':
        break
    last = input('Last name: ')
    if last == 'q':
        break
    user_name = formatted_name(first, last)
    print(f'Hello, {user_name}!')