# Write your solution here
word_1 = input('Please type in a string 1: ')
word_2 = input('Please type in a string 2: ')
l1 = len(word_1)
l2 = len(word_2)
if l1 == l2:
    print(f'The strings are equally long')
elif l1 > l2:
    print(f'{word_1} is longer')
else:
    print(f'{word_2} is longer')