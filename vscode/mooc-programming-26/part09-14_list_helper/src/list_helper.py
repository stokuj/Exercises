# WRITE YOUR SOLUTION HERE:


class ListHelper():

    
    def greatest_frequency(my_list: list) -> int:
        my_dict = {}    
        for number in my_list:
            if number not in my_dict:
                my_dict[number] = 0
            my_dict[number] += 1
        
        most_common = my_list[0]
        for n in my_dict:
            if my_dict[n] > my_dict[most_common]:
                most_common = n
        
        return most_common
    
    def doubles(my_list: list) -> int:
        my_dict = {}    
        for number in my_list:
            if number not in my_dict:
                my_dict[number] = 0
            my_dict[number] += 1
        
        counter = 0
        for n in my_dict:
            if my_dict[n] >= 2:
                counter += 1
        return counter
if __name__ == "__main__":    
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))