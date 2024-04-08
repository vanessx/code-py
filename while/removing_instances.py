pets = ['cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)

for pet in pets:
    print(pet, end = ' ')