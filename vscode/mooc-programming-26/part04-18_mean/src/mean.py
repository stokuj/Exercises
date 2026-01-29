# Write your solution here
def mean(my_list):
    sum = 0
    for x in my_list:
        sum += x
    return sum / len(my_list)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)
    print("mean value is", result)