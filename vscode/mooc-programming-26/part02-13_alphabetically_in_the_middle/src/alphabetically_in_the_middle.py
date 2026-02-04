# Write your solution here

a = input('1st letter:')
b = input('2nd letter:')
c = input('3rd letter:')

if (b>a>c) or (c>a>b):
    print(f'The letter in the middle is {a}')
elif (b>c>a) or (a>c>b):
    print(f'The letter in the middle is {c}')
else:
     print(f'The letter in the middle is {b}')