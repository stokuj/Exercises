# Copy here code of line function from previous exercise
def line(n, text):
    if(len(text)>0):
        print(n*text[0])
    else:
        print(n*'*') 
    
def box_of_hashes(height):
    # You should call function line here with proper parameters
    for x in range(0, height):
        line(10, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
    print()
    box_of_hashes(2)
