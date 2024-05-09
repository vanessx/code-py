# usar lista em uma função
def greet_users(names):
    for name in names:
        print(f'Hello, {name.title()}!')

usernames = ['léa', 'margot', 'paul']
greet_users(usernames)