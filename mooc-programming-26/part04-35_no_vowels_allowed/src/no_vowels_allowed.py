# Write your solution here

def no_vowels(word: str) -> str:
    chars = [char for char in word if char not in ['a', 'e', 'i', 'o', 'u']]
    return "".join(chars)

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))