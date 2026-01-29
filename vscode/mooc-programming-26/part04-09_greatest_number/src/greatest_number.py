# Write your solution here
def greatest_number(a, b, c):
    if a > b:
        if a > c:
            return a # 
        else:
            return c 
    else:
        if b > c:
            return b # 
        else:
            return c 

            
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(greatest_number(3, 4, 1)) # 4
    print(greatest_number(99, -4, 7)) # 99
    print(greatest_number(0, 0, 0)) # 0