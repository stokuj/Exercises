# Write your solution here

while(True):
    word = input('Please type in a string: ')
    if word == '':
        break
    print(word)

    for char in word:
        print('-', end='')
    print('\n')