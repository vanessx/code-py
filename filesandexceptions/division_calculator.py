print('Give me two numbers, and I will divide them.\n'
      'Enter \033[031mq\033[m to quit.')

while True:
    first_num = input('First number:\n')
    if first_num == 'q':
        break
    second_num = input('Second number:\n')
    if second_num == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)