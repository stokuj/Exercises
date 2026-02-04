# Write your solution here
number = int(input("Number: "))
output = ''

#if number % 15 == 0:
#    print('FizzBuzz')
#elif number % 3 == 0:
#    print('Fizz')
#elif number % 5 == 0:
#    print('Buzz')

if number % 3 == 0:
   output += 'Fizz'
if number % 5 == 0:
   output += 'Buzz'
print(output)