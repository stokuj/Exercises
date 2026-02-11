from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(course_attempts : list) -> int:
    return reduce(lambda suma, x : suma + x.credits, course_attempts, 0)

def sum_of_passed_credits(course_attempts : list) -> int:
    filtered = filter(lambda course : course.grade >= 1 , course_attempts)
    return reduce(lambda suma, x : suma + x.credits, filtered, 0)

def average(course_attempts : list) -> int:
    filtered = list(filter(lambda course : course.grade >= 1 , course_attempts))
    x = reduce(lambda suma, x : suma + x.grade, filtered, 0)
    return x / len(filtered)


if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)