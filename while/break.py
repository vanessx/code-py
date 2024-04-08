prompt = 'Please enter the name of a city you have visited:'
prompt += "\n(Enter 'quit' when you are finished.)\n"

while True:
    city = input(prompt).strip().lower()
    if city == 'quit':
        break
    else:
        print(f'I would love to go to {city.title()}.')