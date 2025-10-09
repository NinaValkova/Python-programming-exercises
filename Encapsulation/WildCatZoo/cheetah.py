from animal import Animal

class Cheetah(Animal):
    DEFAULT_MONEY_FOR_CARE = 60

    def __init__(self, name, gender, age):
        self.money_for_care = Cheetah.DEFAULT_MONEY_FOR_CARE
        super().__init__(name, gender, age, self.money_for_care)
