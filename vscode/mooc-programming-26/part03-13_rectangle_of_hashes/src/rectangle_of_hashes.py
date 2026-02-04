# Write your solution here

width = int(input('Width: '))
height = int(input('Height: '))

for row in range(0, height):
    for col in range(0, width):
        print("#", end='')
    print('')