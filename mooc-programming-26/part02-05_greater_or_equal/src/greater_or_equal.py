# Write your solution here
first = int(input('Please type in the first number: '))
another = int(input('Please type in another number: '))

if first > another:
    print(f'The greater number was: {first}')
elif another > first:
    print(f'The greater number was: {another}')
else:
    print('The numbers are equal!')