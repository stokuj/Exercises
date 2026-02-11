# Write your solution here

limit = int(input('Limit: '))

suma = 0
liczba = 1

while suma < limit:
    suma += liczba
    liczba += 1

print(suma)