# Write your solution here
def chessboard(num):

    flag = False
    for row in range(0, num):
        for j in range(0, num):
            if flag == True:
                flag = False
                print(0, end='')
            else:
                flag = True
                print(1, end='')
        print('')
        if num % 2 == 0:
            flag = not flag

# Testing the function
if __name__ == "__main__":
    chessboard(6)
