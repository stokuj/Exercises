def print_student(students: dict, name:str):
    if name not in students:
        print(f'{name}: no such person in the database')
        return
    print(f'{name}:')
    if not students[name]:
        print(' no completed courses')
    else:
        print(f' {len(students[name])} completed courses:')
        grade_sum = 0
        for course in students[name]:
            print(f'  {course[0]} {course[1]}')
            grade_sum += course[1]
        grade_sum = grade_sum / len(students[name])
        print(f' average grade {grade_sum}')
        
def add_student(students: dict, name:str):
    courses = []
    students[name] = courses

def add_course(students: dict, name: str, course: tuple):
    course_name, grade = course
    
    # 1. Ignoruj, jeśli ocena to 0
    if grade == 0:
        return

    courses = students[name]
    found = False

    # 2. Szukaj kursu na liście
    for i in range(len(courses)):
        if courses[i][0] == course_name:
            found = True
            # 3. Aktualizuj tylko, jeśli nowa ocena jest wyższa
            if grade > courses[i][1]:
                courses[i] = (course_name, grade)
            break # Znaleźliśmy kurs, nie trzeba szukać dalej

    # 4. Jeśli nie znaleziono kursu, dodaj go
    if not found:
        courses.append(course)
    
def summary(students: dict):
    most_courses_count = 0
    most_courses_name = ''
    
    best_avg = 0
    best_avg_name = ''

    for name, courses in students.items():
        # 1. Liczba kursów
        if len(courses) > most_courses_count:
            most_courses_count = len(courses)
            most_courses_name = name
            
        # 2. Obliczanie średniej (jeśli są kursy)
        if len(courses) > 0:
            avg = sum(course[1] for course in courses) / len(courses)
            if avg > best_avg:
                best_avg = avg
                best_avg_name = name

    print(f'students {len(students)}')
    print(f'most courses completed {most_courses_count} {most_courses_name}')
    print(f'best average grade {best_avg} {best_avg_name}')


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)