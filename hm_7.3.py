from random import random

sentence = 'Hello, hello'


def second_index(text, letters):
    first_index = text.find(letters)

    if first_index == -1:
        return

    second_index = text.find(letters, first_index + 1)

    return second_index if second_index != -1 else None

print(second_index(sentence, 'lo'))