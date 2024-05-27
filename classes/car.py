"""A set of classes used to represent gas and electric cars."""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def describe_car(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f'This car can go about {range} miles on a full charge.')
    
    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
            print('Upgraded the battery to 100kWh.')
        else:
            print('The battery is already upgraded.')

class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()