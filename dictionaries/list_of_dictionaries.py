aliens = []
# criar 30 alies que serão adicionados à lista vazia
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# alterar os valores
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# mostrar apenas 5
for alien in aliens[:5]:
    print(alien)
# mostrar o total de aliens na lista
print(f'Total number of aliens: {len(aliens)}')