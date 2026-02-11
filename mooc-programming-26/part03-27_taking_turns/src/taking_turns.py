# Write your solution here

number = int(input('Please type in a number: '))

flag = True;
i, j = 1, number
for x in range(1, number+1):

    if flag == True:
        flag = False
        print(i)
        i += 1
    else:
        flag = True
        print(j)
        j -= 1