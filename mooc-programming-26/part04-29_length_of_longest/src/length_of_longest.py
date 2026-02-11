# Write your solution here

def length_of_longest(my_list : list) -> int:
    size = 0
    for word in my_list:
        if len(word) > size:
            size = len(word)
    return size