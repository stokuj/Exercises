def load_file(name: str, is_student: bool) -> dict:
    dictionary = {}

    with open(name) as file:
        next(file) # skip header
        for line in file:
            # strip() usuwa \n i zbędne spacje z obu końców linii
            parts = line.strip().split(';')
            if is_student:
                dictionary[parts[0]] = [parts[1], parts[2]]
            else:
                dictionary[parts[0]] = sum(int(x) for x in parts[1:])
            
    return dictionary

def calc_grade(exercises: dict, exam_points: dict) -> dict:
    grades = {}
    for student in exercises:
        exe_points = exercises[student] // 4
        total_points = exe_points + exam_points[student]
        
        grade = 0
        thresholds = [(28, 5), (24, 4), (21, 3), (18, 2), (15, 1)]
        
        for limit, val in thresholds:
            if total_points >= limit:
                grade = val
                break 
        
        grades[student] = grade
    return grades


option1 = input('Student information: ')
option2 = input('Exercises completed: ')
option3 = input('Exam points: ')
std = load_file(option1, True)
exe = load_file(option2, False)
poi = load_file(option3, False) 
grades = calc_grade(exe, poi)
for student_id in std:
    print(std[student_id][0],std[student_id][1], grades[student_id])
