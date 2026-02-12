def check_number(n: str):
    if len(n) != 9:
        return False
        
    weights = [3, 7, 1, 3, 7, 1, 3, 7]
    total_sum = sum(int(n[i]) * weights[i] for i in range(8))
    
    # Calculate distance to the next multiple of 10
    remainder = total_sum % 10
    if remainder == 0:
        check_digit = 0
    else:
        check_digit = 10 - remainder
        
    return int(n[8]) == check_digit


if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False