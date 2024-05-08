# retornar um dicionário
def build_person(first_name, last_name, age=None):
    person = {'first': first_name.title(), 'last': last_name.title()}
    if age:
        person['age'] = age
    return person

actor = build_person('margot', 'robbie', age=33)
print(actor)