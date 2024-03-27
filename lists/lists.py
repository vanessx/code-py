moto = ['honda', 'yamaha', 'suzuki']
print(moto)

moto.append('ducati') # adiciona ducati ao fim da lista 
print(moto)

cars = []
# adicionar elementos a uma lista vazia
cars.append('tesla')
cars.append('mercedes')
cars.append('bmw')

print(cars)

# armazenando dados na lista usando o loop for
games = []

for c in range(1,4):
    answer = input('A game you like: ').lower().strip()
    games.append(answer)

print(games)