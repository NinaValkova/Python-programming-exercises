resources = []

resource_quantity = {}

command = input()
while command != 'stop':
    resources.append(command)
    command = input()

size = len(resources)
for i in range(0, size, 2):
    key = resources[i]
    value = int(resources[i+1])
    
    if key in resource_quantity:
        resource_quantity[key] += value
    else:
        resource_quantity[key] = value
            

for key, value in  resource_quantity.items():
    print(f'{key} -> {value}')  
    