# Write your solution here
students_on_course = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))

numbers_of_groups = students_on_course // group_size

if (students_on_course % group_size) == 0:
    print(f'Number of groups formed: {numbers_of_groups}')
else:
    print(f'Number of groups formed: {numbers_of_groups+1}')

