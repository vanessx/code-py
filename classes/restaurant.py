class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type
    
    def describe_restaurant(self):
        print(f"\nThe restaurant's name is {self.name.title()}.\n"
              f"The cuisine's type is {self.cuisine}.")

    def open_restaurant(self):
        print(f'The {self.name} is open. Come on in!')

restaurant = Restaurant('aero', 'seafood')
print(f'{restaurant.name.title()}. {restaurant.cuisine}.')

restaurant.describe_restaurant()
restaurant.open_restaurant()

north_restaurant = Restaurant('plate of luck', 'classique')
north_restaurant.describe_restaurant()

south_restaurant = Restaurant('fornier', 'française')
south_restaurant.describe_restaurant()