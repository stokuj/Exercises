# Write your solution here


def prime_numbers():
    yield 2  # First prime number
    
    candidate = 3  # Start checking from 3
    
    while True:
        is_prime = True
        
        # Check if candidate is divisible by any number from 2 to candidate-1
        for divisor in range(2, candidate):
            if candidate % divisor == 0:
                is_prime = False
                break
        
        if is_prime:
            yield candidate
        
        candidate += 1
        
    
if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))