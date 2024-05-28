# abrir um ficheiro que está na mesma pasta
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

# abrir um ficheiro que está em outra pasta (relative file path)
"""
with open('foldername/filename.txt') as file_object:
"""

# abrir um ficheiro que está em outra pasta (absolute file path)
# como são longos é mais fácil atribuir o file path a uma variável
"""
file_path = '/home/vanessx/other_files/text_files/filename.txt'
with open(file_path) as file_object:
"""