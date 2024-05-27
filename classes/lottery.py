from random import choice

rand = [1, 5, 9, 7, 31, 13, 55, 11, 99, 73, 'v', 'l', 's', 'a', 'u']
result = []

print('Any ticket matching these four numbers or letters wins a prize:')

# não queremos repetir números e letras, por isso usamos um loop while
while len(result) < 4:
    pulled_item = choice(rand)
    if pulled_item not in result:
        print(f'We pulled a {pulled_item}!')
        result.append(pulled_item)

