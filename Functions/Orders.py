def getPrice(products_prices:dict):
    price = 0
    
    for key, value in products_prices.items():
       if key == product:
          price = value*quantity
       elif key == product:
          price = value*quantity 
       elif key == product:
           price = value*quantity    
       elif key == product:
           price = value*quantity
        
    return price    
    

product = input()
quantity = int(input())


products_prices = {'coffee':1.50, 'water':1.00, 'coke':1.40, 'snacks': 2.00}

#price = getPrice(products_prices)
price = products_prices[product]*quantity

print(f"{price:.2f}")        
               
        