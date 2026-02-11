# Write your solution here

word = input('Please type in a string: ')
len_word = len(word)

#print(len_word)
#print(20-len_word)

for char in range(0, 20-len_word):
    print('*', end='')

for i in range(0, len_word):
    print(word[i], end='')
