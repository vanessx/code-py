class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"\nThe restaurant's name is {self.name.title()}.\n"
              f"The cuisine's type is {self.cuisine}.\n"
              f"The restaurant has served {self.number_served} customers.")

    def open_restaurant(self):
        print(f'The {self.name} is open. Come on in!')

    def set_number_served(self, customers):
        self.number_served = customers
    
    def increment_number_served(self, add):
        self.number_served += add

restaurant = Restaurant('aero', 'seafood')
print(f'{restaurant.name.title()}. {restaurant.cuisine}.')

restaurant.set_number_served(12)
restaurant.increment_number_served(5)
restaurant.describe_restaurant()
restaurant.open_restaurant()


north_restaurant = Restaurant('plate of luck', 'classique')
north_restaurant.describe_restaurant()


south_restaurant = Restaurant('fornier', 'française')
south_restaurant.describe_restaurant()

