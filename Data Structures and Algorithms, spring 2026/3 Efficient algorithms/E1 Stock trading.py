## Optimization goal:
## The initial solutions repeatedly searched for the minimum price or compared all pairs of days, which caused O(n²) complexity.
## The optimized solution keeps track of the minimum price seen so far during a single pass.
## This allows computing the best profit in O(n) time without redundant comparisons.


# O(n^2)
def best_profit(prices):
    n = len(prices)
    best = 0
    for i in range(n):
        for j in range(i + 1, n):
            best = max(best, prices[j] - prices[i])
    return best


# O(n^2)
def best_profit2(prices):
    n = len(prices)
    best = 0
    for i in range(n):
        min_price = min(prices[0:i+1])
        best = max(best, prices[i] - min_price)
    return best


# O(n)
def best_profit3(prices):
    n = len(prices)
    best = 0
    min_price = prices[0]

    for i in range(1, n):
        best = max(best, prices[i] - min_price)
        min_price = min(min_price, prices[i])

    return best


TESTS = 2000

time1 = 0
time2 = 0
time3 = 0

for _ in range(TESTS):
    n = random.randint(5, 200)
    prices = [random.randint(1, 1000) for _ in range(n)]

    # ---- metoda 1 ----
    start = time.perf_counter()
    r1 = best_profit(prices)
    time1 += time.perf_counter() - start

    # ---- metoda 2 ----
    start = time.perf_counter()
    r2 = best_profit2(prices)
    time2 += time.perf_counter() - start

    # ---- metoda 3 ----
    start = time.perf_counter()
    r3 = best_profit3(prices)
    time3 += time.perf_counter() - start

    # sprawdzenie poprawności
    if r1 != r2 or r1 != r3:
        print("ERROR", prices, r1, r2, r3)
        break

print("\n=== ŚREDNI CZAS ===")
print(f"best_profit  : {time1 / TESTS:.8f}s")
print(f"best_profit2 : {time2 / TESTS:.8f}s")
print(f"best_profit3 : {time3 / TESTS:.8f}s")
