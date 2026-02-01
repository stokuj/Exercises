import urllib.request
import json
import certifi
import ssl

def retrieve_all() -> list:
    active_courses = []
    address = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    
    # Kontekst SSL dla nowszych wersji Pythona
    myssl = ssl.create_default_context(cafile=certifi.where())
    
    response = urllib.request.urlopen(address, context=myssl)
    data = response.read()
    
    # Zabezpieczenie: testy vs prawdziwy internet (bytes vs str)
    if isinstance(data, bytes):
        data = data.decode('utf-8')
        
    data_json = json.loads(data)
    
    for course in data_json:
        if course['enabled'] == True:
            exercise_pts = sum(course['exercises'])
            
            # POPRAWKA TUTAJ: Dodajemy course['year'] jako trzeci element
            active_courses.append((
                course['fullName'], 
                course['name'], 
                course['year'],
                exercise_pts
            ))
            
    return active_courses


def retrieve_course(course_name: str) -> dict:
    address = f'https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats'
    
    # Kontekst SSL
    myssl = ssl.create_default_context(cafile=certifi.where())
    
    response = urllib.request.urlopen(address, context=myssl)
    data = response.read()
    
    # 1. Dekodujemy bajty na tekst i parsujemy JSON
    # Jeśli data to bajty (b'...') zamień na string
    if isinstance(data, bytes):
        data = data.decode('utf-8')
        
    weeks_stats = json.loads(data) # Teraz to jest słownik Pythona
    
    # 2. Inicjalizacja zmiennych
    # weeks_stats wygląda tak: {"0": {...}, "1": {...}}
    # Liczba tygodni to liczba kluczy w tym słowniku
    weeks_count = len(weeks_stats)
    
    max_students = 0
    total_hours = 0
    total_exercises = 0
    
    # 3. Iterujemy po WARTOŚCIACH słownika (czyli po danych dla każdego tygodnia)
    for week in weeks_stats.values():
        # Szukamy maksimum studentów
        if week['students'] > max_students:
            max_students = week['students']
            
        # Sumujemy godziny
        total_hours += week['hour_total']
        
        # Sumujemy ćwiczenia
        total_exercises += week['exercise_total']
        
    # 4. Obliczamy średnie (dzielenie całkowite //)
    # Zabezpieczenie przed dzieleniem przez zero
    if max_students > 0:
        hours_avg = total_hours // max_students
        exercises_avg = total_exercises // max_students
    else:
        hours_avg = 0
        exercises_avg = 0
        
    # 5. Zwracamy wymagany słownik
    return {
        'weeks': weeks_count,
        'students': max_students,
        'hours': total_hours,
        'hours_average': hours_avg,
        'exercises': total_exercises,
        'exercises_average': exercises_avg
    }

# Test
if __name__ == "__main__":
    print(retrieve_course("docker2019"))
    
    print(retrieve_course('docker2019'))