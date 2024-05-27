from car import Car

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