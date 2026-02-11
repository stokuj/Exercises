# Write your solution here

def read_input(text:str, a:int, b:int) -> int:
    while True:
        try:
            number = int(input(text))
            if a < number and number < b:
                return number
            else:
                print(f'You must type in an integer between {a} and {b}')
        except ValueError:
            print(f'You must type in an integer between {a} and {b}')
    pass


if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)