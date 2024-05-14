class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type
    
    def describe_restaurant(self):
        print(f"The restaurant's name is {self.name}.\n"
              f"The cuisine's type is {self.cuisine}.")

    def open_restaurant(self):
        print(f'The {self.name.title()} is open. Come on in!')

restaurant = Restaurant('aero', 'seafood')
print(f'{restaurant.name.title()}. {restaurant.cuisine}.')

restaurant.describe_restaurant()
restaurant.open_restaurant()