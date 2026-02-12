

#O(n*n) becasue index is O(n) itself, and index() returns index of value in the list

def count_sublists(numbers, x):
    count = {0: 1}
    prefix_sum = 0
    result = 0
    
    for i in range(len(numbers)):
        prefix_sum += numbers[i]
        if prefix_sum - x in count:
            result += count[prefix_sum - x]
        
        if prefix_sum not in count:
            count[prefix_sum] = 0
        count[prefix_sum] += 1
        
    return result 


numbers = [1, 2, 1, 3, 5, 4, 3, 1]
print(count_sublists(numbers, 3))



