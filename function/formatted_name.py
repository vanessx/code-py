# return a simple value
# middle name como opcional, por isso atribuimos um default value
def formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()

musician = formatted_name('jimi', 'hendrix')
print(musician)

musician = formatted_name('john', 'hooker', 'lee')
print(musician)