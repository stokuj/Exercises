grades, points_list = [], []
while True:
    
    user_input = input(f'Exam points and exercises completed: ')
    
    if user_input == '' or user_input == ' ':
        break
    else:
        points, exercises = user_input.split()
        points, exercises = int(points), int(exercises)
        total_score = points + exercises//10
        

        if points < 10:
            grade = 0
        elif total_score <= 14:
            grade = 0
        elif total_score <= 17:
            grade = 1
        elif total_score <= 20:
            grade = 2
        elif total_score <= 23:
            grade = 3
        elif total_score <= 27:
            grade = 4
        else:
            grade = 5
            
        grades.append(grade)
        points_list.append(total_score)

points_avg = sum(points_list)/len(points_list)
pass_percentage = 100 - (grades.count(0)/len(grades))*100

print("Statistics:")

print(f'Points average: {points_avg:.1f}')
print(f'Pass percentage: {pass_percentage:.1f}')
print('Grade distribution:')
for i in range(5, -1, -1):
    print(f'  {i}: {"*" * grades.count(i)}')