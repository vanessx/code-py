motorcycles = ['honda', 'yamaha', 'suzuki', 'bmw']
# insere um novo valor na posição desejada fazendo com que os outros valores da lista mudam a posição para a direita
motorcycles.insert(0, 'ducati') 
print(motorcycles)

# remover um item da lista usando o 'del' quando soubermos em que posição o item está
del motorcycles[1]
print(motorcycles)

# remover um item da lista usando 'pop()' faz com que podemos decidir o que fazer com ele depois de removido
popped_motorcyle = motorcycles.pop() # remove o último item
print(motorcycles)
print(popped_motorcyle) # podemos usá-lo para mostrar no ecrã

# remover um item pelo valor usando o remove() e ainda podemos usá-lo depois de remover
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nThe {too_expensive.title()} is too expensive for me.')