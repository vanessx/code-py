# user é um parâmetro
def greet_user(user):
    print(f'Hello, {user.title()}!')

name = input('What is your name? ')
# name é um argumento
greet_user(name)
