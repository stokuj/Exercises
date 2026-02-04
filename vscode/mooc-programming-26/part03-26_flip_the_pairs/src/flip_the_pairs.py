# Write your solution here

number = int(input('Please type in a number: '))

for x in range(1, number):
    if x % 2 != 0:
        print(x+1)
    else:
        print(x-1)

if number % 2 != 0:
    print(number)
else:
    print(number-1)

