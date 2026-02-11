# write your solution here
def largest() -> int:
    with open('numbers.txt') as new_file:
        number = 0
        for line in new_file:
                # strip() usuwa białe znaki (np. enter), a int() zmienia tekst na liczbę
                liczba = int(line.strip())
                if liczba > number:
                    number = liczba
    return number

#print(largest())