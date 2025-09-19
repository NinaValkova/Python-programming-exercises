def read_input(rooms):
    chairs_visitors = []
    
    for i in range(0, rooms, 1):
        line = input()
        
        # *chairs, visitors = line.split(' ') #chairs becomes a list containing one string (like ["XXXX"])
        # chairs = chairs[0]  # take the first element, e.g. "XXXX". Without chairs = chairs[0], the type of chairs is a list of strings - size is 1
        
        line = line.split()
        chairs = line[0]        # string of X’s
        visitors = int(line[1]) # number
        chairs_visitors.append((chairs, visitors))
        
        # chairs_visitors.append((chairs, int(visitors)))
        
    
    return chairs_visitors   
    


rooms = int(input())
chairs_visitors = read_input(rooms)

total_free_chairs = 0
number_of_room = 1
needed_chairs_in_room = 0
for chairs, visitors in chairs_visitors:
    capacity = len(chairs)
    
    size = visitors
    if size > capacity:
        needed_chairs_in_room = size - capacity  
        print(f'{needed_chairs_in_room} more chairs needed in room {number_of_room}')
        
    else:
        free_chairs = capacity - size
        total_free_chairs += free_chairs
        
    number_of_room +=1    

# if total_free_chairs >= 0 and needed_chairs_in_room <= 0: - case when total_free_chairs are 0 
if needed_chairs_in_room <= 0:    
    print(f'Game On, {total_free_chairs} free chairs left')