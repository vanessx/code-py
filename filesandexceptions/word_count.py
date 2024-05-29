def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # usamos 'pass' para não reportar o erro
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {filename} has about {num_words} words.')

filenames = ['text_files/alice.txt', 'text_files/names.txt', 
             'text_files/nothing.txt','text_files/programming.txt']
for file in filenames:
    count_words(file)
