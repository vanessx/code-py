from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    
    def roll_die(self):
        return randint(1, self.sides)

d6 = Die()
results = []

for shot in range(10):
    result = d6.roll_die()
    results.append(result)

print('10 rolls of a 6-sided die:')
for num in results:
    print(num, end=' ')

d10 = Die(10)
results = []

for shot in range(10):
    result = d10.roll_die()
    results.append(result)

print('\n10 rollsof a 10-sided die:')
for num in results:
    print(num, end=' ')

d20 = Die(20)
results = []

for shot in range(10):
    result = d20.roll_die()
    results.append(result)

print('\n10 rolls of a 20-sided die:')
for num in results:
    print(num, end=' ')
