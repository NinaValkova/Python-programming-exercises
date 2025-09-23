from collections import deque

line = input()
names = line.split() # list stores references (pointers) to the string objects "Tracy", "Emily", "Daniel".

n = int(input()) 

# Shallow copy → new container, same object references.
# Modifying the container itself (pop, append, etc.) → only affects that container.
queue = deque(names) # Copies references to the objects in the list ("Tracy", "Emily", "Daniel") into the deque.
                     # Both names[0] and queue[0] point to the same  object in memory - shallow copy

while len(queue) > 1:
  for i in range(0, n-1):
      kid = queue.popleft() # removing an element from one container does not remove it from other containers that point to the same object - Strings are immutable, so you can’t change the object itself.
      queue.append(kid)
  removed_kid = queue.popleft()
  print(f'Removed {removed_kid}')


name = queue[0]
print(f'Last is {name}')    
