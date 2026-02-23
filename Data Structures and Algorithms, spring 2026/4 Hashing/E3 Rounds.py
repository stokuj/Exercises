
import random
import time

#O(n*n) becasue index is O(n) itself, and index() returns index of value in the list
def count_rounds(numbers):
    n = len(numbers)
    
    rounds = 1
    for i in range(1, n):
        if numbers.index(i + 1) < numbers.index(i):
            rounds += 1    
    return rounds

#O(n) since we have O(2n+1)
def count_rounds2(numbers):
    n = len(numbers)
    
    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i
        
    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds

# ===== TEST DLA 10^7 =====
print("Generowanie permutacji 1..10^7...")
n = 10**5
numbers = list(range(1, n + 1))
random.shuffle(numbers)
print(f"Lista zawiera {len(numbers)} elementów")

# ---- metoda 1 (O(n²)) ----
print("\nTestowanie count_rounds (O(n²))...")
start = time.perf_counter()
r1 = count_rounds(numbers)
time1 = time.perf_counter() - start
print(f"Wynik: {r1}")
print(f"Czas: {time1:.4f}s")

# ---- metoda 2 (O(n)) ----
print("\nTestowanie count_rounds2 (O(n))...")
start = time.perf_counter()
r2 = count_rounds2(numbers)
time2 = time.perf_counter() - start
print(f"Wynik: {r2}")
print(f"Czas: {time2:.4f}s")

# ===== PORÓWNANIE =====
print("\n" + "="*50)
print("=== PORÓWNANIE ===")
print(f"count_rounds  (O(n²)): {time1:.4f}s")
print(f"count_rounds2 (O(n)) : {time2:.4f}s")