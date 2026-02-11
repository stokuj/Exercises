# Copy here code of line function from previous exercise
def line(n, text):
    if(len(text)>0):
        print(n*text[0])
    else:
        print(n*'*') 
        
def triangle(size):
    # You should call function line here with proper parameters
    for x in range(1, size+1):
        line(x, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(6)
    print()
    triangle(3)
