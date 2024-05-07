def describe_city(name, country='portugal'):
    print(f'{name.title()} is in {country.title()}.')

describe_city('porto')
describe_city('paris', 'france')
describe_city(name='coimbra')