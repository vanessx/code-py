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
    
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.describe_car())

# mudar o valor de um atributo diretamente
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# mudar o valor de um atributo através de um método (função)
my_new_car.update_odometer(24)
my_new_car.read_odometer()

## outra instância ##
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.describe_car())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

# aumentar o valor do atributo através de um método (função)
my_used_car.increment_odometer(100)
my_used_car.read_odometer()