def read_input():

    line = input()
    command = line.split(": ")
    
    products_quantities = {}
    while command != 'statistics':
        if(command[0] not in products_quantities):
            value = int(command[1])
            products_quantities[command[0]] = value
        else:
            value = int(command[1])
            products_quantities[command[0]] += value
            
        line = input()
        if(line != 'statistics'):
            command = line.split(": ")
        else:
            command = line          
    
    return products_quantities

def print_info(products_quantities):
    print(f'Products in stock:')
    
    total_products = 0
    total_quantity = 0
    for product, quantity in products_quantities.items():
        print(f'- {product}: {quantity}')
        total_products +=1
        total_quantity +=quantity 
        
    print(f'Total Products: {total_products}')   
    print(f'Total Quantity: {total_quantity}') 

products_quantities = read_input()
# print_info(products_quantities)
print(f'Products in stock:')
[print(f'- {product}: {quantity}') for (product, quantity) in products_quantities.items()]
total_products = len(products_quantities.keys())
total_quantity = sum(products_quantities.values())
print(f'Total Products: {total_products}')   
print(f'Total Quantity: {total_quantity}')
        