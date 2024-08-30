
banned_words = ['Turkey', 'Dog', 'Fox', 'Cat', 'Chicken']

def text_filter(message_to_send):
    split_message = message_to_send.split()
    filtered = []
    for text in split_message:
        if text not in banned_words:
            filtered.append(text)
    return " ".join(filtered)

print()
message = input('Enter your message here: ')
print()
print(f'Input message: {message}')

filtered = text_filter(message)

print(f'Output message: {filtered}')
print()
