
my_dict = {}

while True:
    option =  input('command (1 search, 2 add, 3 quit): ')
    if option == '3':
        print('quitting...')
        break
    
    # adding
    elif option == '2':
        name = input('name: ')
        number = input('number: ')
        
        if name not in my_dict:

            my_dict[name] = []
        my_dict[name].append(number)
        
        print('ok!')
    
    #search
    elif option == '1':
        name = input('name: ')

        try:
            size = len(my_dict[name])
            for i in range(size):
                print(my_dict[name][i])
            
        except:
            print('no number')
            
    #wrong input
    else:
        print('Wrong, try again!')