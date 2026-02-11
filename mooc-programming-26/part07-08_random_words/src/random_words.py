# Write your solution here
from random import sample

def load_words() -> list:
    words = []
    with open('words.txt') as file:
        for line in file:
            word = line.strip()
            words.append(word)
    return words

def words(n: int, beginning: str) -> list:
    all_words = load_words()
            
    filtered = [w for w in all_words if w.startswith(beginning)]
    
    if len(filtered) < n:
            raise ValueError(f"Nie znaleziono wystarczającej liczby słów zaczynających się na '{beginning}'")
        
    return sample(filtered, n)
    
if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)