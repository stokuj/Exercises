# Write your solution here
import datetime as datetime

def is_it_valid(pic: str) -> bool:
    CHARS = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    if len(pic) != 11:
        return False

    day = int(pic[0:2])
    month = int(pic[2:4])
    year_short = int(pic[4:6])
    marker = pic[6]
    personal_id = pic[7:10]
    control_char = pic[10]

    # 1. Określamy pełny rok na podstawie markera
    if marker == '+':
        year = 1800 + year_short
    elif marker == '-':
        year = 1900 + year_short
    elif marker == 'A':
        year = 2000 + year_short
    else:
        return False # Nieprawidłowy marker
    try:
        date = datetime.date(year, month, day)
    except ValueError:
        return False # Data nie istnieje (np. 30 lutego)

    # Sklejamy 6 cyfr daty i 3 cyfry ID w jedną liczbę
    combined_number = int(pic[0:6] + pic[7:10])

    # Obliczamy resztę z dzielenia przez 31
    index = combined_number % 31

    # Sprawdzamy, czy wyliczony znak zgadza się z tym w PIC
    if CHARS[index] != control_char:
        return False
    
    return True

if __name__ == "__main__":
    print(is_it_valid('230827-906F'))
    print(is_it_valid('120488+246L'))
    print(is_it_valid('310823A9877'))