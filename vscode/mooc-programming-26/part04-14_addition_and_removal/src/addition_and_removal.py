# Write your solution here

my_list = []
counter = 1
while True:
    print(f'The list is now {my_list}')
    
    option = input('a(d)d, (r)emove or e(x)it: ')
    if option == 'd':
        my_list.insert(len(my_list), counter)
        counter += 1
    elif option == 'r':
        my_list.remove(counter-1)
        counter -= 1
    else:
        break
print('Bye!')