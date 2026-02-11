
while True:
    word = input('Editor: ').lower()

    if word == 'visual studio code':
        print('an excellent choice!')
        break
    elif word == 'notepad' or word == 'word':
        print('awful')
    else:
        print('not good')
        