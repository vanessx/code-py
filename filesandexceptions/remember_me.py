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
        print(f'Welcome back, {username}!')
    else:
        username = new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()