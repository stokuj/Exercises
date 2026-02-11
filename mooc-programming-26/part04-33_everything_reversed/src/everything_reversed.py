def everything_reversed(names: list) -> list:
    # using the global variable instead of the parameter by accident
    size = len(names)
    my_list = []
    for index in range(0, len(names)):
        #print(size-index-1, size, index)
        my_list.append(names[len(names)-index-1][::-1])
    return my_list     

# All the code for testing the function should be within this block
if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
    
    