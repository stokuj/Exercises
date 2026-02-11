# Write your solution here
def same_chars(word, num1, num2):
    try:
        if num2 >= len(word):
            return False
        elif word[num1] == word[num2]:
            return True
        else:
            return False
    except:
        print('Error')
# You can test your function by calling it within the following block
if __name__ == "__main__":
    # same characters m and m
    print(same_chars("programmer", 6, 7)) # True

    # different characters p and r
    print(same_chars("programmer", 0, 4)) # False

    # the second index is not within the string
    print(same_chars("programmer", 0, 12)) # False

    print(same_chars("abc", 0, 3)) # False