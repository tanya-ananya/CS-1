exam_grades = [83, 85, 72, 65, 76, 90, 79, 88, 93, 70, 67, 80]
attendance_day1 = {'Mary', 'Jake', 'Sam', 'Alex', 'Percy', 'Jessica', 'Trent', 'Mahmoud'}
attendance_day2 = {'Jake', 'Sam', 'Alex', 'Percy', 'Mahmoud', 'Trent', 'Caleb', 'Zayne'}

highest_grade = max(exam_grades)
lowest_grade = min(exam_grades)
average_grade = sum(exam_grades)/len(exam_grades)
both_days = set.intersection(attendance_day1, attendance_day2)
one_day = set.symmetric_difference(attendance_day1, attendance_day2)
total_students_exams = len(exam_grades)
total_students = len(both_days) + len(one_day)

print()
print(f'{total_students_exams} Students took the exam.')
print(f'The highest grade was a {highest_grade}')
print(f'The lowest grade was a {lowest_grade}')
print(f'The average grade for the exam was a {average_grade:.1f}')
print()
print(f'{total_students} students attended the class.')
print(f'{both_days} attended both class days.')
print(f'{one_day} attended one class day.')
print()