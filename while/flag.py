# flag
active = True
while active:
    message = prompt = input('Tell me something, and I will repeat it back to you: '
               "\nEnter 'quit' to end the program. ").lower().strip()
    if message == 'quit':
        active = False
    else:
        print(message)