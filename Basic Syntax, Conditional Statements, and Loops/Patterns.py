number = int(input())

# for i in range(0, number):
# #repeat the string * exactly n times 
#      print('*'*(i+1))

# for j in range(number-1, 0, -1):
#      print('*'*(j))

for i in range(1, number+1):
     for j in range(1,i+1):
          print('*', end='')
     print()     

for j in range(number-1, 0, -1):
     for j in range(1,j+1):
          print('*', end='')
     print() 
