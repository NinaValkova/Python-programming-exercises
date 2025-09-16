line = input()

parts = line.split() # ['A-1', 'A-5', 'A-10', 'B-2']
part = [x.split('-') for x in parts] # [['A', '1'], ['A', '5'], ['A', '10'], ['B', '2']]
unique_parts = set()

size = len(part)
for i in range(0, size, 1):
    unique_parts.add(tuple(part[i])) # cannot directly add lists (which are mutable) to a set because sets in Python require their elements to be hashable (i.e., immutable). types, like strings, tuples, and numbers
                                     # [('A', '1'), ('A', '5'), ('A', '10'), ('B', '2'), ('A', '7'), ('A', '3')]

playersA = 11
playersB = 11
flag = True

# set, which is unordered and does not support indexing
for part in unique_parts:
    if part[0] == 'A':
        playersA -=1
    elif part[0] == 'B':
        playersB -=1

    if playersA < 7 or playersB < 7:
        print(f'Team A - {playersA}; Team B - {playersB}')
        print('Game was terminated')  
        flag = False
        break     

if flag:
    print(f'Team A - {playersA}; Team B - {playersB}')