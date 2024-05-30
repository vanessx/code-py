def read_files(filename):
    with open(filename) as files:
        contents = files.read()
    print(contents)

filenames = ['text_files/cats.txt', 'text_files/dogs.txt']
# usamos o for porque não conseguimos abrir ficheiros dentro de uma lista
for file in filenames:
    read_files(file)