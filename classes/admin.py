class User:
    def __init__(self, first_name, last_name, age, gender, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        print(f'Your name is {self.first_name.title()} {self.last_name.title()}'
              f' and you are {self.age} years old.')
        print(f'Your gender is {self.gender} and you live in {self.location.title()}.')

    def greet_user(self):
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}!')

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        print('The privileges are:')
        for privilege in self.privileges:
            print(f'{privilege}')

class Admin(User):
    def __init__(self, first_name, last_name, age, gender, location):
        super().__init__(first_name, last_name, age, gender, location)
        self.privileges = Privileges()