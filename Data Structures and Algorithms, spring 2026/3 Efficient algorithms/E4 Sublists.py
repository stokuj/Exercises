## Optimization goal:

def count_lists(numbers):
    n = len(numbers)
    a = b = -1
    result = 0
    for i in range(1, n):
        if numbers[i] != numbers[i - 1]:
            if numbers[i] != numbers[a]:
                b = a
            a = i - 1
        result += a - b
    return result

nums = [1, 2, 3, 3, 2, 2, 4, 2]

print(count_lists(nums))
