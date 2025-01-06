def second_index(text, letters):
    first_index = text.find(letters)

    if first_index == -1:
        return

    second_index = text.find(letters, first_index + 1)

    return second_index if second_index != -1 else None

sentence = 'Hello, hello'
sentence2 = 'Hello, lo lo lo'

print(second_index(sentence, 'lo'))
print(second_index(sentence2, 'lo'))
