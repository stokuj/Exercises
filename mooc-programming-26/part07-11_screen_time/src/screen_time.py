import datetime

def save_to_file(file_name: str, start_date: datetime.date, formated_start_date: str, total_minutes: int, avg_minutes: float, list_dates: list, days: int):
    
    with open(file_name, 'w') as file:
        end_date = start_date + datetime.timedelta(days=days - 1)
        
        formated_end_date = end_date.strftime("%d.%m.%Y")
        
        file.write(f'Time period: {formated_start_date}-{formated_end_date}\n')
        file.write(f'Total minutes: {total_minutes}\n')
        file.write(f'Average minutes: {avg_minutes:.1f}\n')
        
        current_date = start_date
        
        for day in list_dates:
            current_date_str = current_date.strftime("%d.%m.%Y")
            
            line = f'{current_date_str}: {day[0]}/{day[1]}/{day[2]}\n'
            file.write(line)
            
            current_date += datetime.timedelta(days=1)

# --- Część główna programu ---


file = input('Filename: ')
date_input = input('Starting date: ')
days = int(input('How many days: '))

date_parts = date_input.split('.')

# Tworzymy obiekt daty
start_date = datetime.date(int(date_parts[2]), int(date_parts[1]), int(date_parts[0]))
formated_start_date = start_date.strftime("%d.%m.%Y")

print('Please type in screen time in minutes on each day (TV computer mobile): ')

list_dates = []

# Dodatkowa zmienna pomocnicza do wyświetlania daty przy wpisywaniu
input_date_cursor = start_date 

for _ in range(days):
    # Wyświetlamy datę, o którą pytamy (ładniej wygląda)
    current_date_str = input_date_cursor.strftime("%d.%m.%Y")
    
    line = input(f'Screen time {current_date_str}: ')
    parts = line.split(' ')
    
    # Zabezpieczenie: jeśli ktoś wpisze za mało danych, program się nie wywali
    if len(parts) < 3:
        parts = [0, 0, 0] # Domyślne zera w razie błędu
        print("Błąd danych! Ustawiono 0 0 0.")

    list_dates.append(parts)
    input_date_cursor += datetime.timedelta(days=1)

    
total_minutes = 0

for day in list_dates:
    total_minutes += int(day[0]) + int(day[1]) + int(day[2])

avg_minutes = total_minutes / days

# 5. Przekazujemy 'days' do funkcji
save_to_file(file, start_date, formated_start_date, total_minutes, avg_minutes, list_dates, days)

print(f'Data stored in file {file}')