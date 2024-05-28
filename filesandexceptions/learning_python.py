filename = 'text_files/learning_python.txt'

print('\033[031mEntire file:\033[m')
with open(filename) as file_object:
    content = file_object.read()
print(content)

print('\033[032mLine by line:\033[m')
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print('\033[034mStoring lines in a list:\033[m')
with open(filename) as file_object:
    content = file_object.readlines()

for line in content:
    print(line.rstrip())