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
        print(f"===Input mark for course name: {self.name} ===")

        for stu in students:
            mark = float(input(f"mark for student {stu.name}, id : {stu.id}: "))
            self.marks[stu.id] = mark

    def listMark(self, students):
        print(f"list mark for course: {self.name}")
        for stu in students:
            mark = self.marks.get(stu.id)
            print(f"{stu.name} ({stu.id}): {mark}")

class schoolManeger:
    def __init__(self):
        self.students = []
        self.courses = []
    

    def input_student(self):
        n = int(input("Number of students: "))
        for _ in range(n):
            s = Student()
            s.input()
            self.students.append(s)
    def input_course(self):
        n = int(input("Number of courses: "))
        for _ in range(n):
            c = Course()
            c.input()
            self.courses.append(c)
    def inputMark(self):
        print("\nSelect a course:") 
        for i , c in enumerate(self.courses):
            print(f"{i+1}. {c.name}")
        idx = int(input("Select course index: ")) - 1
        course = self.courses[idx]
        course.inputMark(self.students)

    def listStudent(self):
        print("==============Students===============")
        for s in self.students:
            s.list()
    def listCourse(self):
        print("===============Courses===============")
        for c in self.courses:
            c.list()
    def listMark(self):
        print("================Mark=================")
        for i , c in enumerate(self.courses):
            print(f"{i+1}. {c.name}")
        idx = int(input("Select course index: ")) - 1
        course = self.courses[idx]
        course.listMark(self.students)

def main():
    sm = schoolManeger()
    print("=== INPUT PHASE ===")
    sm.input_student()
    sm.input_course()
    sm.inputMark()
    print("\n=== LISTING PHASE ===")
    sm.listStudent()
    sm.listCourse()
    sm.listMark()


if __name__ == "__main__":
    main()