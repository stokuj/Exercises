# Copy here code of line function from previous exercise
def line(n, text):
    if(len(text)>0):
        print(n*text[0])
    else:
        print(n*'*') 

def square(size, character):
    # You should call function line here with proper parameters
    for x in range(0, size):
        line(size, character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "*")
    print()
    square(3, "o")