filename = 'text_files/programming.txt'
# escrever para um ficheiro novo
# 'w' significa write mode ('r' read mode, 'a' append mode, 'r+' read and write)
with open(filename, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games!\n')
