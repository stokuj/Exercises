# Write your solution here

limit = int(input('Limit: '))

suma = 0
liczba = 1
word = ''
while ( suma < limit):
    suma += liczba

    if (suma  < limit):
        #print(f'{liczba} +')
        word += f'{liczba} + '
    else:
        #print(f'{liczba} =')
        word += f'{liczba} = '

    liczba += 1
print(f'The consecutive sum: {word}{suma}')
