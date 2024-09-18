'''
THis program will take in the names and gpas of students entered by the user and output the number of students and the top student
Author: Taaruni Ananya'''

class EmptyRosterError(Exception):
    pass

class Student:
    def __init__(self, first, last, gpa):
        self.first = first
        self.last = last
        self.gpa = gpa

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def get_gpa(self):
        return self.gpa

class Course:
    def __init__(self):
        self.roster = []

    def add_student(self, student):
        self.roster.append(student)

    def course_size(self):
        return len(self.roster)

    def find_student_highest_gpa(self):
        if not self.roster:
            raise EmptyRosterError('Exception: Course Roster is Empty')
        max_gpa = float()
        top_student = None
        for student in self.roster:
            if student.get_gpa() > max_gpa:
                max_gpa = student.get_gpa()
                top_student = student
        return top_student

def main():
    course = Course()
    
    print("Welcome to CSC/DSCI: Principles in CS/DS I")
    print("Please Add Students to the Course: (quit or q to exit)")
    
    while True:
        first_name = input("Enter First Name: ")
        
        if first_name.lower() == 'quit' or first_name.lower() == 'q':
            break

        last_name = input("Enter Last Name: ")
        
        try:
            gpa = float(input("Enter GPA: "))
        except ValueError:
            print("Error: Enter a Numeric GPA")
            continue

        student = Student(first_name, last_name, gpa)
        course.add_student(student)

    print(f"Course Size: {course.course_size()} students")
    
    try:
        top_student = course.find_student_highest_gpa()
        if top_student:
            print(f"Top Student: {top_student.get_first()} {top_student.get_last()} (GPA: {top_student.get_gpa()})")
        else:
            print("No students in the roster.")
    except EmptyRosterError as excpt:
        print(excpt)

main()
