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

# a classe electriccar é filho da classe car
class ElectricCar(Car):
    # representa aspectos de veicúlos elétricos apenas
    def __init__(self, make, model, year):
        # inicializa os atributos da mãe (class Car)
        super().__init__(make, model, year)
        self.battery_size = 75
    
    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

my_tesla = ElectricCar('tesla', 'model x', 2019)
print(my_tesla.describe_car())
my_tesla.describe_battery()