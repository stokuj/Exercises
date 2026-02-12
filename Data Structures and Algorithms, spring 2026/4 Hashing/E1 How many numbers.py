## Optimization goal:



# O(n^2)
def count_distinct(nums):
    result = []
    for number in nums:
        if number not in result:
            result.append(number)
            
    return len(result)

# O(n)
def count_distinct2(nums):
    seen = set()
    for x in nums:
        seen.add(x)
    return len(seen)

# O(n)
def count_distinct(numbers):
    return len(set(numbers))

nums = [3, 1, 2, 1, 5, 2, 2, 3]

print(count_distinct(nums))
