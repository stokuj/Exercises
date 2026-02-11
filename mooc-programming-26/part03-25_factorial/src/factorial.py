# Write your solution here

while True:
    number = int(input('Please type in a number: '))
    tmp = 1
    if number <= 0:
        print('Thanks and bye!')
        break
    
    for i in range(1, number+1):
        tmp = tmp * i 

    print(f'The factorial of the number {number} is {tmp}')