events = ['coding', 'dog', 'cat', 'movie']

line = input()
count =0
while line != 'END':
    if line.lower() in events:
        if line.islower():
            count+=1
        elif line.isupper():
            count+=2
    line = input()        

if(count > 5):
    print('You need extra sleep')
else:
    print(count)    
