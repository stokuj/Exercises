
import random
import time


def find_mode(numbers):
    result = {}
    
    for number in numbers:
        if number not in result:
            result[number] = 1
        else:
            result[number] += 1
    return max(result, key=result.get)

def find_mode2(numbers):
    count = {}
    mode = (0, 0)

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        mode = max(mode, (count[x], x))

    return mode[1]


numbers = [1, 2, 3, 2, 2, 3, 2, 2]
#find_mode(numbers)



TESTS = 2000

time1 = 0
time2 = 0

for _ in range(TESTS):
    n = random.randint(5, 200)
    prices = [random.randint(1, 1000) for _ in range(n)]

    # ---- metoda 1 ----
    start = time.perf_counter()
    r1 = find_mode(numbers)
    time1 += time.perf_counter() - start

    # ---- metoda 2 ----
    start = time.perf_counter()
    r2 = find_mode2(numbers)
    time2 += time.perf_counter() - start


print("\n=== ŚREDNI CZAS ===")
print(f"find_mode  : {time1 / TESTS:.8f}s")
print(f"find_mode2 : {time2 / TESTS:.8f}s")
