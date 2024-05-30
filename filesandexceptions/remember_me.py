import json
# lemos o username caso já tenha sido fornecido
# caso contrário, perguntamos o username e guardamos
filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What's your name?\n")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f'Welcome back, {username}!')