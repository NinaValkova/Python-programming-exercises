quantity_material = {'shards': 0,
                     'fragments': 0,
                     'motes': 0
                     }

quantity = 0
material = ''
flag = True
while flag:
     line  = input().split()
     
     size = len(line)
     
     for i in range(0, size, 2):
         quantity = int(line[i])
         material = line[i+1].lower()
         
         if material not in quantity_material:
             quantity_material[material] = 0
             quantity_material[material] += quantity
         else:    
             quantity_material[material] += quantity
         
             if quantity_material[material] >= 250:
                 if(material == 'shards'):
                     print('Shadowmourne obtained!')
                     quantity_material[material] -= 250
                     flag = False 
                     break
                 if(material == 'fragments'):
                     print('Valanyr obtained!')
                     quantity_material[material] -= 250
                     flag = False   
                     break   
                 if(material == 'motes'):
                     print('Dragonwrath obtained!')
                     quantity_material[material] -= 250
                     flag = False  
                     break              

# print legendary items first
for key in ["shards", "fragments", "motes"]:
    print(f"{key}: {quantity_material[key]}")

# print junk items sorted alphabetically
for key in quantity_material.keys():
    if key not in ["shards", "fragments", "motes"]:
        print(f"{key}: {quantity_material[key]}")
