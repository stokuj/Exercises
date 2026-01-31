def filter_incorrect():
    # Plik wyjściowy otwieramy w trybie 'w' (write)
    with open('lottery_numbers.csv') as file, open('correct_numbers.csv', 'w') as new_file:
        for line in file:
            original_line = line # Zachowujemy oryginał do zapisu
            parts = line.strip().split(';')
            
            # 1. Sprawdzanie numeru tygodnia
            try:
                week_parts = parts[0].split(' ')
                week_number = int(week_parts[1])
            except (ValueError, IndexError):
                continue # Jeśli to nie liczba lub brakuje części, pomiń linię

            # 2. Sprawdzanie liczb (czy jest ich 7)
            numbers_raw = parts[1].split(',')
            if len(numbers_raw) != 7:
                continue

            # 3. Sprawdzanie poprawności samych liczb
            try:
                num_list = []
                error_found = False
                
                for number_str in numbers_raw:
                    number = int(number_str)
                    
                    # Czy liczba jest w zakresie 1-39?
                    if number < 1 or number > 39:
                        error_found = True
                        break
                    
                    # Czy liczba się powtarza?
                    if number in num_list:
                        error_found = True
                        break
                    
                    num_list.append(number)
                
                if error_found:
                    continue
                    
            except ValueError:
                # To się wykona, jeśli np. zamiast liczby będzie tekst "aaa"
                continue

            # Jeśli kod dotarł tutaj, oznacza to, że linia jest poprawna
            new_file.write(original_line)
if __name__ == "__main__":
    filter_incorrect()