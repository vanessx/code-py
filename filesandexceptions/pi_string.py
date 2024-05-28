"""mexer no conteúdo de um ficheiro"""
filename = 'text_files/pi_digits.txt'

with open(filename) as file_object:
    # o método readlines() pega cada linha e guarda numa lista (neste caso: files))
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))