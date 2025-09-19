def read_input(wagons, train):
    commands = []
    command = ''
    
    line = input()
    while line != 'End':
        command, *args = line.split()
        args = [int(x) for x in args]
        
        # keep all commands like tuple
        commands.append((command, args)) 
        
        line = input()  
    
    return commands    

def printPeople(commands, train, wagons):
   
    # unpack tuple
   for command, values in commands:
       if command == 'add':
           train[-1] += values[0]     
       elif command == 'insert':
           index = values[0]
           element = values[1]
           train[index] += element
       else:
           index = values[0]
           element = values[1]
           train[index] -= element    
           
   print(train)          

wagons = int(input())
train = [0]*wagons

commands = read_input(wagons, train)

printPeople(commands, train, wagons)