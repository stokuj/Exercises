
def load_dict() -> dict:
    dictionary = {}
    with open('dictionary.txt') as file:
        for line in file:
            parts = line.strip().split(':')
            dictionary[parts[0]] = parts[1]
    return dictionary

def add_word(dictionary:dict, word_finish: str, word_english: str):
    with open('dictionary.txt', 'a') as file:
        line = f'{word_finish}:{word_english}\n'
        file.write(line)
        dictionary[word_finish] = word_english
      
def search(dictionary:dict, word: str):
    for finish, english in dictionary.items():
        if word in finish or word in english:
            print(f'{finish} - {english}')



dictionary = load_dict()
while True:
    print('1 - Add word, 2 - Search, 3 - Quit')
    option1 = input('Function: ')

    if option1 == '1':
        entry1 = input('The word in Finnish: ')
        entry2 = input('The word in English: ')
        add_word(dictionary, entry1, entry2)
        print('Dictionary entry added')
    elif option1 == '2':
        term = input('Search term: ')
        search(dictionary, term)
    else:
        print('Bye!')
        break
                    
                    