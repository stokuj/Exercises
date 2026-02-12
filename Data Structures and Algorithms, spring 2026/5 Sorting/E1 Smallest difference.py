
# O(n*log(n))
def min_diff(numbers):
    numbers = sorted(numbers)

    result = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        result = min(result, numbers[i] - numbers[i - 1])
    
    return result


x = [4, 1, 7, 3, 9]

print(min_diff(x))