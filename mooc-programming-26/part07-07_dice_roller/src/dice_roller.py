# Write your solution here
from random import choice

def roll(die: str):
    list_a = [3, 3, 3, 3, 3, 6]
    list_b = [2, 2, 2, 5, 5, 5]
    list_c = [1, 4, 4, 4, 4, 4]
    
    if die == 'A':
        return choice(list_a)
    elif die == 'B':
        return choice(list_b)
    elif die == 'C':
        return choice(list_c)
    else:
        return 0

def play(die1: str, die2: str, times: int) -> tuple:
    result = [0, 0, 0]
    
    for i in range(times):
        if roll(die1) == roll(die2):
            result[2] += 1
        elif roll(die1) > roll(die2):
            result[0] += 1  
        else:
            result[1] += 1
        
    return (result[0], result[1], result[2])
if __name__ == "__main__":
    # for i in range(20):
    #     print(roll("A"), " ", end="")
    # print()
    # for i in range(20):
    #     print(roll("B"), " ", end="")
    # print()
    # for i in range(20):
    #     print(roll("C"), " ", end="")
    
    result = play("A", "B", 100)
    print(result)
    result = play("B", "B", 1000)
    print(result)