def readAnimals():
    line = input()
    animals = line.split(', ')

    return animals


animals = readAnimals()
size = len(animals)

if animals[-1] == "wolf":  
    print("Please go away and stop eating my sheep")
else:
    # Warn the sheep in front of the wolf that it is about to be eaten
    wolf_index = animals.index("wolf")
    sheep_index = (len(animals) - wolf_index) - 1
    print(f"Oi! Sheep number {sheep_index}! You are about to be eaten by a wolf!")