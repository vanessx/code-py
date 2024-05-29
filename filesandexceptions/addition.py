try:
    first_num = int(input('First number:\n'))
    second_num = int(input('Second number:\n'))
except ValueError:
    # caso o user introduza letras
    print('Please, enter numbers.')
else:
    result = first_num + second_num
    print(f'The sum of {first_num} and {second_num} is \033[031m{result}\033[m.')