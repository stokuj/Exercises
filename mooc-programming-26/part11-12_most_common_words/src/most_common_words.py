# WRITE YOUR SOLUTION HERE:


import string


def most_common_words(filename: str, lower_limit: int) -> dict:
    
    my_dict = {}
    with open(filename) as file:
        for line in file:
            parts = line.strip().split()
            
            for word in parts:
                word = word.strip(string.punctuation)
                if word not in my_dict:
                    my_dict[word] = 1
                else:
                    my_dict[word] += 1   
    return {word : my_dict[word] for word in my_dict if my_dict[word] >= lower_limit}

# x = most_common_words("comprehensions.txt", 3)
# print(x)