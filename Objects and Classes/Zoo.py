class Mammals:
    def __init__(self):
        super().__init__() 
        self._mammals = []

    def add_mammal(self, mammal):
        self._mammals.append(mammal)

    def get_mammal(self):
        return self._mammals


class Fishes:
    def __init__(self):
        super().__init__()
        self._fishes = []

    def add_fishes(self, fish):
        self._fishes.append(fish)    

    def get_fishes(self):
        return self._fishes    


class Birds:
    def __init__(self):
        super().__init__()
        self._birds = []
    
    def add_birds(self, bird):
        self._birds.append(bird) 
    
    def get_birds(self):
        return self._birds;                          


class Zoo(Mammals, Fishes, Birds):
    __animals = 0

    def __init__(self, name):
        super().__init__() 
        self.Name = name

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, name):
        self._name = name

    def add_animal(self, species, name):
        if species == 'mammal':
            self.add_mammal(name)
        elif species == 'fish':    
            self.add_fishes(name)
        elif species == 'bird':
            self.add_birds(name)  

        # This refers to a class variable. It belongs to the class itself, not to any particular instance
        Zoo.__animals += 1

    @classmethod
    def get_count(cls):
        return cls.__animals    

    def get_info(self, species):
        species_array = []
        if species == 'mammal':
            species_array = self.get_mammal()
            species_name = 'Mammals'
        elif species == 'fish':    
            species_array = self.get_fishes()
            species_name = 'Fishes'
        elif species == 'bird':
            species_array = self.get_birds()
            species_name = 'Birds'

        final_list = ", ".join(species_array)
        return (
            f"{species_name} in {self.Name}: {final_list}\nTotal animals: {Zoo.get_count()}"
        )


class ReadInput:
    @staticmethod
    def read_input():
        name_of_zoo = input()

        zoo = Zoo(name_of_zoo)
        capacity = int(input())

        for i in range(0, capacity):
            command = input().split(" ")
            species = command[0]
            name = command[1]
            zoo.add_animal(species, name)  
        
        return zoo    


zoo = ReadInput.read_input()
type = input()
print(zoo.get_info(type))
