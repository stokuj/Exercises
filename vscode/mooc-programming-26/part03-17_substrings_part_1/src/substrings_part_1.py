# Write your solution here

word = input('Please type in a string: ')

len_word = len(word)
for index in range(0, len_word):
    print(word[0:index+1])