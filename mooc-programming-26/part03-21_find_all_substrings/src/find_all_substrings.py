# Write your solution here

word = input('Please type in a word: ')
char = input('Please type in a character: ')


for i, x in enumerate(word):
    if x == char:
        #This code  will be executed n times,
        # where n is number of chars in string 'word'

        if(i+2 < len(word)):
            print(word[i:i+3])