# Write your solution here
def load_words() -> list:
    with open('words.txt') as file:
        words = []
        for line in file:
            words.append(line.replace('\n',''))
            
    return words

      
def find_words(search_term: str) -> list:
    words = load_words()
    found_words = []
    
    for word in words:
        if '.' in search_term:
            if len(search_term) == len(word):
                flag = True
                for i in range(len(search_term)):
                    if search_term[i] != '.' and search_term[i] != word[i]:
                        flag = False
                if flag:
                    found_words.append(word)
        elif '*' in search_term:
            if '*' in search_term[0]:
                if word.lower().endswith(search_term[1:]):
                    found_words.append(word)
            else:
                if word.lower().startswith(search_term[:-1]):
                    found_words.append(word)
        else:
            if word.lower() == search_term:
                found_words.append(word)

    return found_words

    
#print(find_words("c.t"))