alien_color = input('Alien color: ')

if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
elif alien_color == 'red':
    points = 15
else:
    points = 0
    print('Try again. Choose a color between green, yellow and red.')

print(f'You just earned {points} points!')