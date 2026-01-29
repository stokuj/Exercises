# Write your solution here
def spruce(num):
    print('a spruce!')
    for i in range(0, num):
        
        row = ' '*(num-(1+i))+ '*'*(1+i*2) + ' '*(num-(1+i))
        print(row)
    row = ' '*(num-(1))+ '*'*(1) + ' '*(num-(1))
    print(row)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)