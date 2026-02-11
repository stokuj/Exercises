# Write your solution here

word = input('Please type in a string: ')
sub  = input('Please type in a substring: ')

if sub in word:
    index = word.find(sub)
    word = word[index+len(sub):]
    #print(word, index, sub)
    
    if sub in word:
        index2 = word.find(sub)
        word = word[index2:]
        print(f'The second occurrence of the substring is at index {index+index2+len(sub)}.')
    else:
        print('The substring does not occur twice in the string.')
else:
    print('The substring does not occur twice in the string.')