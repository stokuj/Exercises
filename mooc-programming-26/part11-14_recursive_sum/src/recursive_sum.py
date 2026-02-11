# WRITE YOUR SOLUTION HERE:


def recursive_sum(number: int):
    # if the number is 1, there is nothing else to add
    if number <= 1:
        return number

    return recursive_sum(number-1) + number 

# print(recursive_sum(3))