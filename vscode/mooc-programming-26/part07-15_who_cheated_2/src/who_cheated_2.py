import csv
from datetime import datetime, timedelta

def final_points() -> dict:
    start_times = {} 
    points_by_task = {} # Struktura: { 'student': { 'zadanie1': 5, 'zadanie2': 6 } }
    
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
            task = line[1]
            points = int(line[2])
            submission_time_str = line[3]
            
            if name not in start_times:
                continue
                
            submission_time = datetime.strptime(submission_time_str, "%H:%M")
            start_time = start_times[name]
            
            difference = submission_time - start_time

            if difference > timedelta(hours=3):
                continue
            
            # --- POPRAWKA GŁÓWNA (Twój błąd KeyError) ---
            # Zanim odwołasz się do points_by_task[name], musisz upewnić się, że klucz istnieje.
            if name not in points_by_task:
                points_by_task[name] = {}  # Tworzymy pustą "teczkę" na zadania
            
            # Teraz możemy bezpiecznie sprawdzać points_by_task[name][task]
            # (bo wiemy, że points_by_task[name] już istnieje)
            if task not in points_by_task[name] or points > points_by_task[name][task]:
                points_by_task[name][task] = points

    # 3. Sumowanie punktów
    final_grades = {}
    for name, tasks_dictionary in points_by_task.items():
        final_grades[name] = sum(tasks_dictionary.values())

    return final_grades

if __name__ == "__main__":
    print(final_points())