

#O(n*n) becasue index is O(n) itself, and index() returns index of value in the list
def count_rounds(numbers):
    n = len(numbers)
    
    rounds = 1
    for i in range(1, n):
        if numbers.index(i + 1) < numbers.index(i):
            rounds += 1    
    return rounds

#O(n) since we have O(2n+1)
def count_rounds2(numbers):
    n = len(numbers)
    
    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i
        
    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds
numbers = [3,4,5,1,2,6,8,7,9]
print(count_rounds2(numbers))



