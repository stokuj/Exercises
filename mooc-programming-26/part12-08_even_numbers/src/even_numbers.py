# Write your solution here


def  even_numbers(beginning: int, maximum: int) -> int:
    num = beginning
    while num <= maximum:
        if num % 2 == 0:
            yield num
        num +=1
        
        
        
if __name__ == "__main__":    
    numbers = even_numbers(11, 21)
    for number in numbers:
        print(number)