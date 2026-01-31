

def write_file(filename: str, text: str):
    with open(filename, 'a') as file:
        file.write(f'{text}\n')

def read_file(filename:str):
    with open(filename) as file:
        for line in file:
            print(line)
    
while True:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    option1 = input('Function: ')

    if option1 == '1':
        entry = input('Diary entry: ')
        write_file('diary.txt', entry)
        print('Diary saved')
        
    elif option1 == '2':
        read_file('diary.txt')
    else:
        print('Bye now!')
        break
                    
                    