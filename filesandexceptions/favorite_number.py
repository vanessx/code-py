import json

filename = 'fac_num.json'

try:
    with open(filename) as f:
        num = json.load(f)
except FileNotFoundError:
    num = input("What's your favorite number?\n")
    with open(filename, 'w') as f:
        json.dump(num, f)
    print('Noted!')
else:
    print(f'Your favorite num is {num}.')

