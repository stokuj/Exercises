# Write your solution here
from random import randint, choice
from string import ascii_lowercase, digits

def generate_strong_password(how_many: int, has_numbers: bool, has_special: bool) -> str:
    SPECIALS = "!?=+-()#"
    
    characters = [choice(ascii_lowercase)]
    if has_numbers:
        characters.append(choice(digits)) 
    if has_special:
        characters.append(choice(SPECIALS)) 
    
    pool = ascii_lowercase
    if has_numbers:
        pool += digits
    if has_special:
        pool += SPECIALS

    password = "" 
        
    while len(characters) < how_many:
            characters.append(choice(pool))
        
    return "".join(characters)

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))