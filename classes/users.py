class User:
    def __init__(self, first_name, last_name, age, gender, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.location = location
    
    def describe_user(self):
        print(f'Your name is {self.first_name.title()} {self.last_name.title()}'
              f'and you are {self.age} years old.')
        print(f'Your gender is {self.gender} and you live in {self.location.title()}.')

    def greet_user(self):
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}!')

user1 = User('léa', 'seydoux', 38, 'female', 'paris')
user1.greet_user()
user1.describe_user()

print()

user2 = User('margot', 'robbie', 33, 'female', 'los angeles')
user2.greet_user()
user2.describe_user()

print()

user3 = User('tom', 'ackerley', 33, 'male', 'london')
user3.greet_user()
user3.describe_user()