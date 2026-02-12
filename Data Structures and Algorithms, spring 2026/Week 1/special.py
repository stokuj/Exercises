def check_year(year):
    a = year // 100
    b = year - a * 100
    return year == (a + b) ** 2
    
    
if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False