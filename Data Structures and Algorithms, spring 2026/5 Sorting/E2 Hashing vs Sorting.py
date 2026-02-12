
# O(n)
def count_distinct_set(numbers):
    seen = set()

    for x in numbers:
        seen.add(x)

    return len(seen)

#O(n log(n))
def count_distinct_sort(numbers):
    numbers = sorted(numbers)
   
    result = 1
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1]:
            result += 1

    return result

nums = [3, 1, 2, 1, 5, 2, 2, 3]

print(count_distinct_sort(nums))