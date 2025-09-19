electrons = int(input())

electrons_list = []

n = 1
while electrons > 0:
    max_electrons = 2 * pow(n, 2) 
    
    if max_electrons <= electrons:
        electrons_list.append(max_electrons)
        electrons -=max_electrons
    else:
        electrons_list.append(electrons)
        break    
    n+=1    
        
print(electrons_list)        
  