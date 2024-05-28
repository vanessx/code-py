filename = 'text_files/guest_book.txt'

print('Write \033[031mquit\033[m when you are finished.')
while True:
    name = input('What is your name?\n')
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as file:
            file.write(f"{name}\n")
        print(f"Hi, {name.title()}! You've been added to the guest book.")