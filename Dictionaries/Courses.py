line = input()

course_student = {}

while line != 'end':
    command = line.split(' : ')
    course = command[0]
    student = command[1]
    
    if course not in course_student:
        course_student[course] = [student]
    else:
        course_student[course].append(student)  
         
    line = input()     
    
for course, student in course_student.items():
    number_of_students = len(student)
    print(f'{course}: {number_of_students}')
    for i in range(0, number_of_students):
        print(f'-- {student[i]}')