# Write your solution here
pass_1 = input('Password: ')

while True:
    pass_2 = input('Repeat password: ')
    
    if pass_1== pass_2:
        break
    else:
        print('They do not match!')

print('User account created!')
