from printing_functions import print_models

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