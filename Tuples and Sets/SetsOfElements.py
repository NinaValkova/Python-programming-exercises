def read_input(main_set, size):
    for i in range(0, size):
       number = input()
       main_set.add(number)

line = input().split()
n = int(line[0])
m = int(line[1])

first_set = set()
second_set = set()

read_input(first_set, n)
read_input(second_set, m)


# common_elements = first_set & second_set
common_elements = first_set.intersection(second_set)
for element in common_elements:
    print(element)