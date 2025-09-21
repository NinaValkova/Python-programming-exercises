def is_found(product, products_quantities):
    for prod in products_quantities.keys():
        if prod == product:
            return True
    return False    
    

def find_product(products, products_quantities):
    size = len(products)
    for i in range(0, size, 1):
            if is_found(products[i], products_quantities):
                quantity = products_quantities[products[i]]
                product = products[i]
                print(f'We have {quantity} of {product} left')
            else:
                product = products[i]
                print(f"Sorry, we don't have {product}")    


line = input()
elements = line.split()

products = input().split()

products_quantities = {}

size = len(elements)
for i in range(0, size, 2):
    key = elements[i]
    value = elements[i+1]
    
    products_quantities[key] = value

find_product(products, products_quantities)    