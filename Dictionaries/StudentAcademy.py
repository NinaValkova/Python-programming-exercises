n = int(input())

name_grades = {}

for i in range(0, n, 1):
    name = input()
    grade = float(input())
    
    if name not in name_grades:
        name_grades[name] = [grade]
    else:
         name_grades[name].append(grade)  

for name, grade in name_grades.items():
    average = sum(grade) / len(grade) 
    if average >= 4.5:
        print(f'{name} -> {average:.2f}')
        
              