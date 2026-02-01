import csv
from datetime import datetime, timedelta

def cheaters() -> list:
    start_times = {} # Słownik: { 'imię': obiekt_czasu_startu }
    cheating_students = []
    
    # 1. Wczytujemy czasy startu
    with open('start_times.csv') as my_file:
        for line in csv.reader(my_file, delimiter=";"):
            name = line[0]
            time_str = line[1]

            start_times[name] = datetime.strptime(time_str, "%H:%M")
            
    # 2. Sprawdzamy zgłoszenia
    with open('submissions.csv') as other_file:
        for line in csv.reader(other_file, delimiter=';'):
            name = line[0]
            submission_time_str = line[3] # Czas wysłania zadania
                
            # Zamieniamy czas zgłoszenia na obiekt czasu
            submission_time = datetime.strptime(submission_time_str, "%H:%M")
            start_time = start_times[name]
            
            difference = submission_time - start_time

            if difference > timedelta(hours=3):
                if name not in cheating_students:
                    cheating_students.append(name)

    return cheating_students

if __name__ == "__main__":
    print(cheaters())