# Write your solution here

word = input('Please type in a string: ')

len_word = len(word)
for index in range(0, len_word):

    #print(index, ' ',len_word-index-1, ' ', end='')

    print(word[len_word-index-1:len_word])