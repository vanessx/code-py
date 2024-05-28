filename = 'text_files/learning_python.txt'

with open(filename) as file:
    lines = file.readlines()
# alterar conteúdo de um ficheiro
for line in lines:
    new_line = line.replace('Python', 'C')
    print(new_line.rstrip())
