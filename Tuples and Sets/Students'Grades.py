# n = int(input())

# name_grades = {}
# for i in range(0, n):
#     line = input().split()
#     name = line[0]
#     grade = float(line[1])
    
#     if name not in name_grades:
#         name_grades[name] = [grade]
#     else:
#         name_grades[name].append(grade) 
           
# for name, grades in name_grades.items():
#     average = 0 
#     grades_formatted = ' '.join(f"{g:.2f}" for g in grades)
#     size = len(grades)
#     for i in range(0, size):
#         average += grades[i]
#     average = sum(grades) / len(grades)    
#     print(f'{name} -> {grades_formatted} (avg: {average:.2f})') 
    

    
n = int(input())  

line = tuple(input().split() for i in range(n))
line = tuple((name, float(grade)) for name, grade in line)

unique_names = set(name for name, _ in line) # Tuples can go into a set() because they’re immutable, so Python can hash them.
for name in unique_names:
    grades = tuple(grade for n, grade in line if name == n)
    grades_formatted = ' '.join(f"{g:.2f}" for g in grades)
    average = sum(grades) / len(grades)
    
    print(f'{name} -> {grades_formatted} (avg: {average:.2f})') 