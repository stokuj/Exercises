# Write your solution here

year = int(input('Year: '))
tmp = year + 1
while True:
    if (tmp % 400 == 0) or (tmp % 4 == 0 and tmp % 100 != 0):
        print(f'The next leap year after {year} is {tmp}')
        break
    else:
        tmp = tmp + 1