# Write your solution here

word = input('Please type in a string: ')

len_of_word = len(word)

## if
#print(f'{word[1]} {word[len_of_word-2]}')

if(word[1] == word[len_of_word-2]):
    print(f'The second and the second to last characters are {word[1]}')
else:
    print(f'The second and the second to last characters are different')