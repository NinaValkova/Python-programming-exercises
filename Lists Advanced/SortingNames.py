def sort_names(names):
    sorted_names = names
    size = len(sorted_names)
    
    # (-len(x), x) means: sort by longest length first, and if equal length, sort alphabetically.
    # sorted_names = sorted(names, key=lambda x: (-len(x), x))

    for i in range(0, size, 1):
        for j in range(0, size-i-1):
            if len(sorted_names[j]) < len(sorted_names[j+1]):
                sorted_names[j], sorted_names[j+1] = sorted_names[j+1], sorted_names[j]
            
            elif len(sorted_names[j]) == len(sorted_names[j+1]) and sorted_names[j] > sorted_names[j+1]:
                 sorted_names[j], sorted_names[j + 1] = sorted_names[j + 1], sorted_names[j]
    
    return sorted_names
    
    

line = input()
names = line.split(', ')

sorted_names = sort_names(names)
print(sorted_names)