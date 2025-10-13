class Shop:
    DEFAULT_CAPACITY = 10
    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity):
        self.__capacity = capacity

    # Can access class variables? - No
    # Can modify class variables? - No
    # Creates new instances? - No
    # Used for - Utility/helper functions related to the class
    @staticmethod
    def small_shop(name: str, type: str): 
        return Shop(name, type, Shop.DEFAULT_CAPACITY)

    def add_item(self, item_name: str):  
        size = sum(self.items.values())
        if self.capacity <= size:
            return "Not enough capacity in the shop"

        if item_name not in self.items.keys():  
            self.items[item_name] = 1
        else:
            self.items[item_name] += 1

        return f"{item_name} added to the shop"

    def remove_item(self, item_name:str, amount:int):
        if item_name not in self.items.keys() or amount > self.items[item_name]:
            return f"Cannot remove {amount} {item_name}"

        self.items[item_name] -= amount

        if self.items[item_name] == 0:
            # del self.items[item_name]
            self.items.pop(item_name)

        return f"{amount} {item_name} removed from the shop"

    # it’s the default method Python calls if __str__ is not defined.
    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)
