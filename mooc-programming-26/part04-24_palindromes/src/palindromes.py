# Write your solution here

def palindromes(word : str) -> bool:

    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    else:
        return False
        
# Note, that at this time the main program should not be written inside  
# if __name__ == "__main__":
# block!

while True:
    word = input('Please type in a palindrome: ')
    
    if not palindromes(word):
        print("that wasn't a palindrome")
    else:
        print(f'{word} is a palindrome!')
        break