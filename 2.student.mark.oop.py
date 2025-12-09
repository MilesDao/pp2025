'''
Practical work 1: student mark management
• Functions
• Input functions:
• Input number of students in a class
• Input student information: id, name, DoB
• Input number of courses
• Input course information: id, name
• Select a course, input marks for student in this course
• Listing functions:
• List courses
• List students
• Show student marks for a given course
• Push your work to corresponding forked Github repository
Listing functions: • List courses 
• List students 
• Show student marks for a given course Make it OOP’ed 
• Same functions • Proper attributes and methods 
• Proper encapsulation • Proper polymorphism • e.g. .input(), .list() methods
'''
class Person: 
    def __init__(self):
        self.id = None
        self.name = None
        self.dob = None

    def input(self):
        pass
    def list(self):
        pass

class Student(Person):
    def __init__(self):
        super().__init__()
    def input(self):
        self.name = input("Enter student name: ")
        self.id = input("Enter student id: ")
        self.dob = input("Enter student Dob: ")
    def list(self):
        print(f"Student: ID: {self.id} | Name: {self.name} | DoB: {self.dob}")


class Course:
    def __init__(self):
        self.name = None
        self.id = None
        self.marks = {}

    def input(self):
        self.id = input("Input courses id: ")
        self.name = input("Input courses name: ")
    def list(self):
        print(f"Course: ID: {self.id} | Name: {self.name}")
    
    def inputMark(self, students):
        print(f"===Input mark for course name: {self.name}===")
        for stu in students:
            mark = float(input(f"Mark for {stu.name} ({stu.id}): "))
            self.marks[stu.id] = mark

    def show_marks(self, students):
        print(f"\nMarks for course {self.name}:")
        for stu in students:
            mark = self.marks.get(stu.id, "N/A")
            print(f"{stu.name} ({stu.id}): {mark}")


class SchoolManager:
    def __init__(self):
        self.students = []
        self.courses = []


    def input_students(self):
        n = int(input("Number of students: "))
        for _ in range(n):
            s = Student()
            s.input()
            self.students.append(s)

    def input_courses(self):
        n = int(input("Number of courses: "))
        for _ in range(n):
            c = Course()
            c.input()
            self.courses.append(c)

    def select_course_and_input_marks(self):
        print("\nSelect a course:")
        for i, c in enumerate(self.courses):
            print(f"{i+1}. {c.name}")
        idx = int(input("Select course index: ")) - 1
        course = self.courses[idx]
        course.inputMark(self.students)


    def list_courses(self):
        print("\n--- Course List ---")
        for c in self.courses:
            c.list()

    def list_students(self):
        print("\n--- Student List ---")
        for s in self.students:
            s.list()

    def show_marks_for_course(self):
        print("\nSelect a course to show marks:")
        for i, c in enumerate(self.courses):
            print(f"{i+1}. {c.name}")
        idx = int(input("Select course index: ")) - 1
        course = self.courses[idx]
        course.show_marks(self.students)



def main():
    sm = SchoolManager()

    print("=== INPUT PHASE ===")
    sm.input_students()
    sm.input_courses()
    sm.select_course_and_input_marks()

    print("\n=== LISTING PHASE ===")
    sm.list_students()
    sm.list_courses()
    sm.show_marks_for_course()


if __name__ == "__main__":
    main()