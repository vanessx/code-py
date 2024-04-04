favorite_numbers = {
    'rosamund': [1, 3],
    'léa': [7, 2, 10],
    'vanessa': [5, 1, 9],
    'paul': [13, 26],
    'daniel': [6],
    }

for person, numbers in favorite_numbers.items():
    print(f"\n{person.title()}'s favorite numbers are:", end=" ")
    for number in numbers:
        print(f'{number}', end=" ")

#print(f"Rosamund's favorite number is {favorite_numbers['rosamund']}.")
#print(f"Léa's favorite number is {favorite_numbers['léa']}.")
#print(f"Vanessa's favorite number is {favorite_numbers['vanessa']}.")
#print(f"Paul's favorite number is {favorite_numbers['paul']}.")
#print(f"Daniel's favorite number is {favorite_numbers['daniel']}.")