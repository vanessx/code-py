filename = 'text_files/programming.txt'
# adicionar texto ao ficheiro existente ('a' append)
with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a brownser.\n')
