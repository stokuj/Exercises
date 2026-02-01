# Write your solution here
import string

def string_helper() -> str:
    
    pass

def split_in_half(orig_string: str) -> tuple:

    size = len(orig_string) // 2
    new_str1 = orig_string[:size]
    new_str2 = orig_string[size:]
            
    return (new_str1, new_str2)    


def remove_special_characters(orig_string: str) -> str:
    new_str = ''

    for char in orig_string:
        if char.isalnum() or char == ' ':
            new_str += char
    return new_str     

def change_case(orig_string: str) -> str:
    new_str = ''

    for char in orig_string:
        if char in string.ascii_uppercase:
            new_str += char.lower()
        else:
            new_str += char.upper()
    return new_str      
            
