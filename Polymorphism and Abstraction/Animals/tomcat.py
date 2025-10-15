from cat import Cat

class Tomcat(Cat):
    GENDER = "Male"
    def __init__(self, name, age):
        self.gender = Tomcat.GENDER
        super().__init__(name, age, Tomcat.GENDER)

    def make_sound(self):
        return "Hiss"
