# Write your solution here

print('Please type in integer numbers. Type in 0 to finish.')


counter = 0
sum = 0
mean = 0
positive = 0
negative = 0
while True:
    number = int(input('Number: '))

    if number == 0:
        break
    else:
        counter += 1
        sum += number
        if number > 0:
            positive += 1
        else:
            negative += 1
print(counter)
mean = float(sum)/float(counter)

print(f'Numbers typed in {counter}')
print(f'The sum of the numbers is {sum}')
print(f'The mean of the numbers is {mean}')
print(f'Positive numbers {positive}')
print(f'Negative numbers {negative}')





