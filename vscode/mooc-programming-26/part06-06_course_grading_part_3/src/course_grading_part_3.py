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
    grades_points = {}
    for student in exercises:
        number_of_exe = exercises[student]
        exe_points = number_of_exe // 4
        total_points = exe_points + exam_points[student]
        
        grade = 0
        thresholds = [(28, 5), (24, 4), (21, 3), (18, 2), (15, 1)]
        
        for limit, val in thresholds:
            if total_points >= limit:
                grade = val
                break 
        
        grades_points[student] = [number_of_exe, exe_points, exam_points[student], total_points, grade,]
    return grades_points

def print_stats(s_id: id, students:dict, exercises: dict, exam_points: dict, grades: dict):
    
    first_name, last_name = students[s_id]
    
    exec_nbr, exec_pts, exm_pts, tot_pts, grade = grades[s_id][0], grades[s_id][1], grades[s_id][2], grades[s_id][3], grades[s_id][4]
    name = first_name + ' ' + last_name
    print(f"{name:<30}{exec_nbr:<10}{exec_pts:<10}{exm_pts:<10}{tot_pts:<10}{grade:<10}")


option1 = input('Student information: ')
option2 = input('Exercises completed: ')
option3 = input('Exam points: ')
# option1 = 'students1.csv'
# option2 = 'exercises1.csv'
# option3 = 'exam_points1.csv'


std = load_file(option1, True)
exe = load_file(option2, False)
poi = load_file(option3, False) 

grades = calc_grade(exe, poi)

print(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}")
for s_id in std:
    print_stats(s_id, std, exe, poi, grades)
