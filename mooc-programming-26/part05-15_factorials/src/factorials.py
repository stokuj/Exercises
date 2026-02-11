def factorial(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

def factorials(n: int) -> dict:
    dictionary = {}
    
    for i in range(1, n+1):
        dictionary[i] = factorial(i)

    #print(dictionary)
    return dictionary

# k = factorials(5)
# print(k[1])
# print(k[3])
# print(k[5])