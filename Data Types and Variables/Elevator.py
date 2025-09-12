# people = int(input())
# capacity = int(input())

# courseCount = 0
# while people > 0:
#     people -= capacity
#     courseCount +=1

# print(courseCount)



# people = int(input())
# capacity = int(input())

# courses = people // capacity
# if people % capacity != 0:
#     courses += 1

# print(courses)

import math

people = int(input())
capacity = int(input())

courses = math.ceil(people/capacity)
print(courses)