def show_messages(texts):
    for text in texts:
        print(text)

def send_messages(texts, sent_texts):
    while texts:
        current_text = texts.pop()
        print(f'Sending message: {current_text}.')
        sent_texts.append(current_text)

msg = ['i love movies', 'do you want pizza or lasagna?', 
       'cats are the best', 'python?']
show_messages(msg)
# usar uma cópia da lista na chamada da função
sent_msg = []
send_messages(msg[:], sent_msg)

print('\nFinal list:')
print(msg)
print(sent_msg)