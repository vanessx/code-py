filename = 'text_files/programming_poll.txt'

answers = []

print("Enter \033[031mquit\033[m to quit.")
while True:
    answer = input('Why do you like programming?\n')
    if answer == 'quit':
        break
    else:
        answers.append(answer)

with open(filename, 'a') as file:
    for answer in answers:
        file.write(f'{answer}\n')