from animals.animal import Mammal

class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        
    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if type(food).__name__ == "Fruit" or type(food).__name__ == "Vegetable":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity

        self.weight += 0.10 * food.quantity


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        
    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if type(food).__name__ == "Seed" or type(food).__name__ == "Fruit" or type(food).__name__ == "Vegetable":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity

        self.weight += 0.40 * food.quantity


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if type(food).__name__ == "Seed" or type(food).__name__ == "Fruit":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity

        self.weight += 0.30 * food.quantity


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if type(food).__name__ == "Seed" or type(food).__name__ == "Fruit" or type(food).__name__ == "Vegetable":
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity

        self.weight += 1.00 * food.quantity
