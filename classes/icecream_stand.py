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

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []
    
    def show_flavors(self):
        print(f'The flavors are:', end=' ')
        for flavor in self.flavors:
            print(f'{flavor}', end=' ')

icecream = IceCreamStand('icy', 'ice cream')
icecream.describe_restaurant()
icecream.flavors = ['vanilla', 'banana', 'mint']
icecream.show_flavors()