from random import randint
def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    
    my_list = []
    
    #for i in range(amount):
    while len(my_list) < amount:
        number = randint(lower, upper)
        if number not in my_list:
            my_list.append(number)
    return sorted(my_list)

if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)