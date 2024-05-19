class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def describe_car(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.describe_car())