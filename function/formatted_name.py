# return a simple value
def formatted_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()

musician = formatted_name('jimi', 'hendrix')
print(musician)