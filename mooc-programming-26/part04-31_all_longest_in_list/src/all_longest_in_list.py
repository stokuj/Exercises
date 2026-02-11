# Write your solution here

def all_the_longest(my_list : list) -> list:
    size = 0
    new_list = []
    for word in my_list:
        if len(word) > size:
            size = len(word)
    for word in my_list:
        if len(word) == size:
            print(len(word), size)
            new_list.append(word)
    return new_list

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result) # ['eleventh']