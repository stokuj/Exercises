# Write your solution here

word = input('Word: ')

#First line
for char in range(0, 30):
    print('*', end='')
print('')

#Middle
#print(28-len(word))
for x in range(0, 28-len(word)):
    if x % 2 == 0:
        word = word + ' '
    else:
        word = ' ' + word
print('*' + word + '*')

#Last line
for char in range(0, 30):
    print('*', end='')
print('')