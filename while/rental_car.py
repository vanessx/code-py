car = input('What kind of rental car you would like? ').lower().strip()
if car == 'mercedes':
    mercedes = f'{car}-Benz'
    print(f'Let me see if I can find you a {mercedes.title()}.')
elif car == 'bmw':
    print(f'Let me see if I can find you a {car.upper()}.')
else:
    print(f'Let me see if I can find you a {car.title()}.')