# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
    # Tworzymy listę zawierającą ułamek 1/3 powtórzony 
    # 
    # 
    # amount' razy
    return [Fraction(1, amount) for _ in range(amount)]
if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))