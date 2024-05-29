print('Press \033[031mq\033[m to quit.')
while True:
    try:
        first_num = input('First number:\n')
        if first_num == 'q':
            break
        first_num = int(first_num)

        second_num = input('Second number:\n')
        if second_num == 'q':
            break
        second_num = int(second_num)

    except ValueError:
        # caso o user introduza letras
        print('Please, enter numbers.')
    else:
        result = first_num + second_num
        print(f'The sum of {first_num} and {second_num} is \033[031m{result}\033[m.')