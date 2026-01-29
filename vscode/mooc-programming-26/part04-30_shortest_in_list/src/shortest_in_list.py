# Write your solution here

def shortest(my_list : list) -> str:
    size = len(my_list[0])
    name = ''
    for word in my_list:
        if len(word) < size:
            size = len(word)
            name = word
    return name

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)

    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)