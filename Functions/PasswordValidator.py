def print_error(password):
    flag = True 
    
    size = len(password)
    if size < 6 or size > 10:
      print(f'Password must be between 6 and 10 characters')
      flag = False   
    
    if not is_alnum:    
      print(f'Password must consist only of letters and digits') 
      flag = False   
     
    if counter < 2:
      print(f'Password must have at least 2 digits')
      flag = False   
    
    return flag   
    

password = input()

is_alnum = password.isalnum()

counter = 0
for character in password:
    if character.isdigit():
        counter+=1

flag = print_error(password)

if flag:
    print(f'Password is valid')
    
    
                   