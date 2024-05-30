filenames = ['text_files/cats.txt', 'text_files/dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("\033[031mSorry, I can't find the file.\033[m")