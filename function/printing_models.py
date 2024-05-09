def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print('The following models have been printed:')
    for model in completed_models:
        print(model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# para que a lista original nao seja alterada, fazemos uma cópia usando [:]
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)