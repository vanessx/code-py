import json

def get_stored_username():
    """vai buscar o username se possível"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def new_username():
    """prompt para um user novo"""
    username = input("What's your name?\n")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """dá as boas vindas ao user pelo username"""
    username = get_stored_username()

    if username:
        print('Press \033[032my\033[m to confirm.\n'
          'Press \033[031mn\033[m to register your username.')
        answer = input(f'The username "{username}" is yours?\n')
        if answer == 'y':
            print(f'Welcome back, {username}!')
            return
            # qualquer 'return' vazio diz ao python para abandonar a função
            # sem executar o resto do código

    username = new_username()
    print(f"We'll remember you when you come back, {username}!")

greet_user()