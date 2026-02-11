# Write your solution here
option1 = input('Whom should I sign this to: ')
option2 = input('Where shall I save it: ')

with open(option2, 'w') as file:
    file.write(f'Hi {option1}, we hope you enjoy learning Python with us! Best, Mooc.fi Team')
