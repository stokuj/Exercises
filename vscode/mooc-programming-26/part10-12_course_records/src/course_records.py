class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self._name = name
        self._grade = grade
        self._credits = credits
    
    def __str__(self):
        return f'{self.name} ({self.credits} cr) grade {self.grade}'
    
    @property
    def name(self):
        return self._name
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, n: int):
        self._grade = n
    
    @property
    def credits(self):
        return self._credits
    
    
class CourseRecord():
    def __init__(self):
        self._courses = {} #dictionary will hold course objects

    def add_entry(self, name: str, grade: int, credits: int):
        
        #check if course is NOT in courses 
        if name not in self._courses:
            self._courses[name] = Course(name, grade, credits)  # new object,   name: course_object
            return
        
        #grade in course is max(grade, course_grade)
        self._courses[name].grade = max(self._courses[name].grade, grade)

    def get_entry(self, name: str) -> Course:

        if name in self._courses:
            return self._courses[name]
        return None

    def get_all_entries(self):
        return list(self._courses.values())
    
class CourseRecordApp():
    def __init__(self):
        self.__course_record = CourseRecord()
    
    def help(self):
        print('1 add course')
        print('2 get course data')
        print('3 statistics')
        print('0 exit')
    
    def run(self):
        self.help()
        
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.print_stats()
            else:
                self.help()
                
    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        
        self.__course_record.add_entry(name, grade, credits)
        
    def get_course_data(self):
        name = input("course: ")
        course_obj = self.__course_record.get_entry(name)
        if course_obj == None:
            print('no entry for this course')
        else:
            print(course_obj)
            
    def print_stats(self):
            courses = self.__course_record.get_all_entries()
            if not courses:
                print("No courses recorded yet.")
                return

            num_courses = len(courses)
            total_credits = sum(c.credits for c in courses)
            
            # Obliczanie średniej: suma(ocena * kredyty) / suma(kredyty)
            # Lub prosta średnia arytmetyczna (zależnie od wymagań, tutaj prosta):
            mean = sum(c.grade for c in courses) / num_courses

            # Przygotowanie rozkładu ocen (od 5 do 1)
            grades = [c.grade for c in courses]
            
            print(f"{num_courses} completed courses, a total of {total_credits} credits")
            print(f"mean {mean:.1f}")
            print("grade distribution")
            
            for g in range(5, 0, -1):
                count = grades.count(g)
                stars = "x" * count
                print(f"{g}: {stars}")
            
        
app = CourseRecordApp()
app.run()