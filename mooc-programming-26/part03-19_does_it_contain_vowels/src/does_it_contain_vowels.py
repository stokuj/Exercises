# Write your solution here

word = input('Please type in a string:')
for x in ['a', 'e', 'o']:
    if x in word:
        print(f'{x} found')
    else:
        print(f'{x} not found')