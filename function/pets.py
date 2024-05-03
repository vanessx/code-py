def describe_pet(animal_type, pet_name):
    # mostrar informação sobre o animal de estimação
    print(f'I have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")
# argumentos
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# podemos usar keyword arguments para não cair no erro de trocar a ordem de argumentos
def cat_info(cat_name, cat_age):
    print(f'The name of the cat is {cat_name.title()}.\n'
          f'Its age is {cat_age}.')

cat_info(cat_name='yaya', cat_age='4')