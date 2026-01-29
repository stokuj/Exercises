# Write your solution here
def line(n, text):
    if(len(text)>0):
        print(n*text[0])
    else:
        print(n*'*') 
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(7, "%")
    line(10, "LOL")
    line(3, "")