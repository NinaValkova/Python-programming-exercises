from animal import Animal

class Lion(Animal):
    DEFAULT_MONEY_FOR_CARE = 50

    def __init__(self, name, gender, age):
        self.money_for_care = Lion.DEFAULT_MONEY_FOR_CARE
        super().__init__(name, gender, age, self.money_for_care)
