message = ''

while message != 'quit':
    message = prompt = input('Tell me something, and I will repeat it back to you: '
               "\nEnter 'quit' to end the program. ")
    if message != 'quit':
        print(message)