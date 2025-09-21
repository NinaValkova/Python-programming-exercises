# line = input()
# elements = line.split()

# product_price = {}
# products = []

# while line != 'buy':
#     elements = line.split()
    
#     name = elements[0]
#     price = float(elements[1])
#     quantity = float(elements[2])
#     products.append([name, price, quantity])
    
#     line = input()

# product_quantity = {}
# for name, price, quantity in products:
#     if name not in product_price:
#         product_price[name] = price
#         product_quantity[name] = quantity
#     else:
#          product_price[name] = price
#          product_quantity[name] += quantity
            

# for product, price in product_price.items():
#     final_price = price * product_quantity[product]
#     print(f'{product} -> {final_price:.2f}')
    
 
products = {}  # nested dictionary

line = input()
while line != "buy":
    name, price, quantity = line.split()
    price = float(price)
    quantity = int(quantity)

    # if product is new, create nested dictionary
    if name not in products:
        products[name] = {"price": price, "quantity": quantity}
    else:
        # update latest price and accumulate quantity
        products[name]["price"] = price
        products[name]["quantity"] += quantity

    line = input()

# calculate total price and print
for name, data in products.items():
    total_price = data["price"] * data["quantity"]
    print(f"{name} -> {total_price:.2f}")
   