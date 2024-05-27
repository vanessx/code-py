from restaurant import Restaurant

restaurant = Restaurant('aero', 'seafood')
print(f'{restaurant.name.title()}. {restaurant.cuisine}.')

restaurant.set_number_served(12)
restaurant.increment_number_served(5)
restaurant.describe_restaurant()
restaurant.open_restaurant()