def load_students(name: str) -> dict:
    students = {}

    with open(name) as file:
        next(file) # skip header
        for line in file:
            # strip() usuwa \n i zbędne spacje z obu końców linii
            parts = line.strip().split(';')
            students[parts[0]] = [parts[1], parts[2]]
            
    return students
    
def load_exercises(name: str) -> dict:
    exercises = {}

    with open(name) as file:
        next(file) # skip header
        for line in file:
            # strip() usuwa \n i zbędne spacje z obu końców linii
            parts = line.strip().split(';')
            
            exercises[parts[0]] = sum(int(x) for x in parts[1:])
            
    return exercises
    

# std = load_students('students1.csv')
# exe = load_exercises('exercises1.csv')  
# for student in std:
#     print(std[student][0],std[student][1], exe[student] )
option1 = input('Student information: ')
option2 = input('Exercises completed: ')
std = load_students(option1)
exe = load_exercises(option2)

for student in std:
    print(std[student][0],std[student][1], exe[student] )
    