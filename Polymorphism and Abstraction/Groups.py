class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        size = len(self.people)
        return size

    def __add__(self, other):
        name = f"{self.name} {other.name}"
        people = self.people + other.people

        return Group(name, people)

    def __repr__(self):
        members = ", ".join([str(person) for person in self.people])
        return f"Group {self.name} with members {members}"

    # Return one item by index	group[0]
    def __getitem__(self, index):
        person = self.people[index]
        return f"Person {index}: {person}"

    # Return all items for iteration for person in group:
    def __iter__(self):
        for i, person in enumerate(self.people):
            # Used in __iter__ to produce items one by one
            # Generator behavior
            yield f"Person {i}: {person}"


p0 = Person("Aliko", "Dangote")
p1 = Person("Bill", "Gates")
p2 = Person("Warren", "Buffet")
p3 = Person("Elon", "Musk")
p4 = p2 + p3

first_group = Group("__VIP__", [p0, p1, p2])
second_group = Group("Special", [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

# Python internally calls third_group.__getitem__(index) repeatedly with index = 0, 1, 2… until it gets an IndexError.
# Whatever __getitem__ returns becomes the value of person in the loop.
# but i can use also __iter__
for person in third_group:
    print(person)
