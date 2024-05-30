def common_words(filename, word):
    try:
        with open(filename) as file:
            text = file.read()
    except FileNotFoundError:
        pass
    else:
        count_words = text.lower().count(word)
        print(count_words)

common_words('text_files/valor_do_trabalho.txt', 'trabalho')