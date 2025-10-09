# Name mangling - "private” behavior in Python"
# Internally, self.__name becomes _Person__name.


class Person:
    def __init__(self, name, age):
        self.name = name  # calls the property setter
        self.age = age

    @property
    def name(self):
        return self.__name  # returns the mangled attribute

    @name.setter
    def name(self, name):
        self.__name = name  # sets the mangled attribute

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def get_name(self):
        return self.name  # self.name → triggers @property name() → return self.__name
        # self.name inside get_name() just delegates to the property

    def get_age(self):
        return self.age


person = Person("George", 32)
print(person.get_name())
print(person.get_age())
