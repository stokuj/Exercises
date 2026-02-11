# Write your solution here

gift = int(input('Value of gift: '))
tax = 0

if (0 < gift <= 5000):
    print('No tax!')
    
elif (5000 < gift <= 25000):
    tax = 100 + (gift - 5000) * 0.08
    print(f'Amount of tax: {tax}')

elif (25000 < gift <= 55000):
    tax = 1700 + (gift - 25000) * 0.10
    print(f'Amount of tax: {tax}')

elif (55000 < gift <= 200000):
    tax = 4700 + (gift - 55000) * 0.12
    print(f'Amount of tax: {tax}')

elif (200000 < gift <= 1000000 ):
    tax = 22100 + (gift - 200000) * 0.15
    print(f'Amount of tax: {tax}')
else:
    tax = 142100 + (gift - 1000000) * 0.17
    print(f'Amount of tax: {tax}')
