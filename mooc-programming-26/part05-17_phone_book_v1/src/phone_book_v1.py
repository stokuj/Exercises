
my_dict = {}

while True:
    option =  input('command (1 search, 2 add, 3 quit): ')
    if option == '3':
        print('quitting...')
        break
    elif option == '2':
        name = input('name: ')
        number = input('number: ')
        my_dict[name] = number
        print('ok!')
    elif option == '1':
        name = input('name: ')
        try:
            print(my_dict[name])
        except:
            print('no number')
    else:
        print('Wrong, try again!')