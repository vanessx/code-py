def make_sandwich(*items):
    print('\nThe list of items on a sandwich:')
    for item in items:
        print(f'- {item}')

make_sandwich('onion')
make_sandwich('tuna', 'egg', 'tomatoes', 'sauce')
make_sandwich('chicken', 'two eggs')