## Optimization goal:
## The initial solution recalculated sums of list slices in every iteration, which caused O(n²) time complexity.
## The optimization removes repeated summing and slicing by keeping a running prefix sum and using the total sum of the list.
## This reduces the algorithm to O(n) time by avoiding redundant work.


# O(n²), because computing the two sums takes O(n) time.
def count_splits(nums: list):
    result = 0    
    for index in range(len(nums)-1):
        left_sum= sum(nums[:index+1])
        right_sum = sum(nums[index+1:])
        if left_sum == right_sum :
            result += 1   
    return result

# O(n²)    
def count_splits2(numbers):
    result = 0    
    left_sum = 0
    for index in range(len(nums)-1):
        left_sum += numbers[index]
        right_sum = sum(nums[index+1:])
        if left_sum == right_sum :
            result += 1   
    return result

# O(n)   
def count_splits3(numbers):
    result = 0    
    left_sum = 0
    sum_of_list = sum(numbers)
    for index in range(len(nums)-1):
        left_sum += numbers[index]
        right_sum = sum_of_list - left_sum
        if left_sum == right_sum :
            result += 1   
    return result
nums = [1 , -1, 1, -1, 1, -1, 1, -1]

print(count_splits3(nums))
