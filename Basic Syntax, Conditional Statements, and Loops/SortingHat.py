name = input()

namesCount_houses = {
    1: "Gryffindor", 2: "Gryffindor", 3: "Gryffindor", 4: "Gryffindor",
    5: "Slytherin",
    6: "Ravenclaw"
}

output = []
while name != 'Welcome!':
    size = len(name)

    if name == 'Voldemort':
      output.append('You must not speak of that name!')
      break

    house = namesCount_houses.get(len(name), "Hufflepuff")
    output.append(f"{name} goes to {house}.")

    name = input() 
else:
     output.append('Welcome to Hogwarts.')         

# print("\n".join(output))

for line in output:
    print(line)
