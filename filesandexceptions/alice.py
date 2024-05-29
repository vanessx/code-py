filename = 'text_files/alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f'Sorry, the file {filename} does not exist.')
else:
    # contar o número aproximado de palavras que o ficheiro contêm
    words = contents.split()
    num_words = len(words)
    print(f'The file {filename} has about {num_words} words.')