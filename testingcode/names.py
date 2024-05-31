from name_function import get_formatted_name

print('Enter \033[031mq\033[m to quit.')

while True:
    first = input('First name:\n')
    if first == 'q':
        break
    last = input('Last name:\n')
    if last == 'q':
        break
    print(get_formatted_name(first, last))