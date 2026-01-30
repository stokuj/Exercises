def invert(dictionary: dict):
    # 1. Tworzymy tymczasowy odwrócony słownik
    inverted = {v: k for k, v in dictionary.items()}
    
    # 2. Czyścimy oryginalny słownik (odpowiednik usuwania zawartości list[:])
    dictionary.clear()
    
    # 3. Wypełniamy go nowymi danymi
    dictionary.update(inverted)



# s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
# invert(s)
# print(s)