import difflib

def load_words() -> list:
    with open('wordlist.txt') as file:
        words = []
        for line in file:
            words.append(line.replace('\n',''))
            
    return words

def spellcheck(text: str) -> str:
    words = load_words()
    parts = text.split()
    suggestions = []                                      # collect suggestions separately
    for word in parts:
        if word.lower() in words:
            print(f'{word} ', end='')
        else:
            print(f'*{word}* ', end='')
            
            close_words_list = difflib.get_close_matches(word.lower(), words)
            close_words_str = ''
            for w in close_words_list:
                close_words_str += f'{w}, '
            suggestions.append(f'{word}: {close_words_str}')  # save for later

    print()                                               # newline after the main output
    for s in suggestions:                                 
        print(f'suggestions:\n{s}')


text = input('Write text: ')

spellcheck(text)