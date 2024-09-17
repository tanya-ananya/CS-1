''' 
This program will take in information about students and produce the user's desired output from the information

Author: Taaruni Ananya
'''
class EmptyRosterError(Exception):
    pass

class Student:
    def __init__(self, gpa, first, last):
        self.gpa = gpa
        self.first = first
        self.last = last

    def get_gpa(self):
        return self.gpa
    
    def get_first(self):
        return self.first
    
    def get_last(self):
        return self.last
    
class Course: 
    def __init__(self):
        self.roster = []

    def add_student(self, student):
        self.roster.append(student)
    
    def course_size(self):
        len(self.roster)
    
    def find_student_highest_gpa(self):
        if not self.roster:
            raise EmptyRosterError('Exception: course roster is empty.')
        
        
        
def main():

   course = Course()
   user_input = ''

   while user_input != 'q':
    first = input("Please enter the student's first name: ")
    last = input("Please enter the student's last name: ")
    
    try:
        gpa = float(input("Please enter the student's GPA: "))
    except ValueError as excpt:
        print(excpt)
        print('Invalid entry to GPA.')
        continue
    
    student = Student(gpa, first, last)
    course.add_student(student)

    user_input = input("Please enter a key ('q' to quit'): ")

    print(f'Number of students enrolled in program: {course.course_size}')
    try:
        highest_gpa = course.find_student_highest_gpa()
    except EmptyRosterError as excpt:
        print('Exception: Course Roster is Empty.')

main()