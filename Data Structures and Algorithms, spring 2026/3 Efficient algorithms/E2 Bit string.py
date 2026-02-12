## Optimization goal:
## The original solution checked every possible pair of indices using nested loops, resulting in O(n²) complexity.
## The optimized version counts zeros seen so far while iterating once through the string.
## When a '1' is encountered, it adds the number of previous zeros, reducing the complexity to O(n).


# O(n^2)
def count_ways(bits):
    n = len(bits)
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            if bits[i] == '0' and bits[j] == '1':
                result += 1
    return result

# O(n)
def count_ways2(bits):
    n = len(bits)
    result = 0
    zeros = 0
    for i in range(n):
        if bits[i] == '0':
            zeros += 1
        if bits[i] == '1':
            result += zeros
    return result

bits = "01001011"

print(count_ways2(bits))
