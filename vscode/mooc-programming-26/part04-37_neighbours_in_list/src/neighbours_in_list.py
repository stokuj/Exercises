# Write your solution here
def longest_series_of_neighbours(my_list: list) -> int:
    counter  = 0
    max_counter = 0
    for index in range(1, len(my_list)):
        if abs(my_list[index-1]- my_list[index]) <= 1 :
            counter +=1
        else:
            counter = 0

        if counter > max_counter:
            max_counter = counter
        #print(my_list[index-1], my_list[index], counter, max_counter)
    return max_counter + 1


if __name__ == "__main__":
    my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))