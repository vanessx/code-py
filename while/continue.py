current_number = 0
# usar continue em um loop
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0: # se o numero for divisivel continua para o print caso contrário retorna
        continue
    print(current_number)