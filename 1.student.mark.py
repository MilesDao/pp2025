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

'''


class Students:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Mark:
    def __init__(self, sid, cid, mark):
        self.sid = sid
        self.cid = cid
        self.mark = mark


def inputStudent():
    n = int(input("Number of students: "))
    students = []
    for i in range(n):
        sid = input("Student ID: ")
        name = input("Student name: ")
        DoB = input("DoB: ")

        students.append(Students(sid, name, DoB))
    return students


def inputCourse():
    n = int(input("Number of courses: "))
    courses = []
    for i in range(n):
        cid = input("Course ID: ")
        name = input("Course name: ")
        courses.append(Course(cid, name))
    return courses


def inputMark(students, courses, marks):
    cid = input("Select a course ID: ")

    # Check if course exists
    if not any(c.id == cid for c in courses):
        print("Invalid course ID!")
        return

    print(f"Entering marks for course {cid}...")

    for s in students:
        m = float(input(f"Mark for {s.name} ({s.id}): "))
        marks.append(Mark(s.id, cid, m))


def listCourse(courses):
    print("\nCourses:")
    for c in courses:
        print(f"{c.id} | {c.name}")


def listStudent(students):
    print("\nStudents:")
    for s in students:
        print(f"{s.id} | {s.name} | {s.DoB}")


def listMark(marks, students, course_id):
    print(f"\nMarks for course {course_id}:")

    found = False
    for m in marks:
        if m.cid == course_id:
            st = next((s for s in students if s.id == m.sid), None)
            if st:
                print(f"{st.name} ({st.id}): {m.mark}")
                found = True

    if not found:
        print("No marks recorded for this course.")


def main():
    students = []
    courses = []
    marks = []

    while True:
        print("\n--- MENU ---")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks for a course")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks of a course")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            students = inputStudent()
        elif choice == "2":
            courses = inputCourse()
        elif choice == "3":
            inputMark(students, courses, marks)
        elif choice == "4":
            listStudent(students)
        elif choice == "5":
            listCourse(courses)
        elif choice == "6":
            cid = input("Enter course ID: ")
            listMark(marks, students, cid)
        elif choice == "0":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
