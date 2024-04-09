answers = {}

active = True

while active:
    name = input('What is your name? ')
    place = input('If you could visit one place in the world, where would '
                  'you go? ')
    answers[name] = place
    repeat = input('Do you want to continue? (yes/or)').strip().lower()
    if repeat == 'no':
        active = False

for name, place in answers.items():
    print(f'{name.title()} would like to go to {place.title()}!')