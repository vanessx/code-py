from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model x', 2019)
print(my_tesla.describe_car())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()