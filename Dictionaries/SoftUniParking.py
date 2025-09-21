n = int(input())

users_licenseNumber = {} 

for i in range(0, n, 1):
    line = input()
    
    command = line.split()
    
    if command[0] == 'register':
        name = command[1]
        if name not in users_licenseNumber:
            licenseNumber = command[2]
        
            users_licenseNumber[name] = licenseNumber
         
            print(f'{name} registered {licenseNumber} successfully')
        else:
            print(f'ERROR: already registered with plate number {licenseNumber}')    
    else: 
       name = command[1]
       if name in users_licenseNumber:
           users_licenseNumber.pop(name)
           print(f'{name} unregistered successfully')
       else:
           print(f'ERROR: user {name} not found')    
       
for user, licenseNumber in users_licenseNumber.items():
    print(f'{user} => {licenseNumber}')    
    
    