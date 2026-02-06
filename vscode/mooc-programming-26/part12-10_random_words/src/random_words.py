# Write your solution here:

import random


def word_generator(characters: str, length: int, amount: int):
    for i in range(amount)
        word = ''.join(random.choice(characters) for i in range(length))
        yield word

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 10)
    for word in wordgen:
        print(word)