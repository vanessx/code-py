def print_models(unprinted_designs, completed_models):
# printa todo o conteúdo de uma lista e adiciona noutra
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing model: {current_design}')
        completed_models.append(current_design)