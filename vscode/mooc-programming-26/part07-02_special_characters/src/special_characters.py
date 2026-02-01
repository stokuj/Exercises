
def separate_characters(my_string: str) -> tuple:
    import string
    ASCII = string.ascii_letters
    PUNCTUATION = string.punctuation
    string1 = ''
    string2 = ''
    string3 = '' 
    
    for char in my_string:
        if char in ASCII:
            string1 += char
        elif char in PUNCTUATION:
            string2 += char
        else:
            string3 += char
            
    return (string1, string2, string3)

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])