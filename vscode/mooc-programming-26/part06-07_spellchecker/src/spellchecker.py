# write your solution here

def load_words() -> list:
    with open('wordlist.txt') as file:
        words = []
        for line in file:
            words.append(line.replace('\n',''))
            
    return words

def spellcheck(text: str) -> bool:
    words = load_words()
    parts = text.split()
    for word in parts:
        if word.lower() in words:
            print(f'{word} ', end='')
        else:
            print(f'*{word}* ', end='')

text = input('Write text: ')
#text = 'We use ptython to make a spell checker'

spellcheck(text)

