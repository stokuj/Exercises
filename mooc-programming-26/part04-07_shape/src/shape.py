# Copy here code of line function from previous exercise
def line(n, text):
    if(len(text)>0):
        print(n*text[0])
    else:
        print(n*'*') 
        
def shape(num, char, num2, char2):
    for x in range(1, num+1):
        line(x, char)
    for x in range(1, num2+1):
        line(num, char2)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")
