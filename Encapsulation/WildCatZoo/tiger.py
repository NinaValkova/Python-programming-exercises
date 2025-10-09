from animal import Animal

class Tiger(Animal):
    DEFAULT_MONEY_FOR_CARE = 45

    def __init__(self, name, gender, age):
        self.money_for_care = Tiger.DEFAULT_MONEY_FOR_CARE
        super().__init__(name, gender, age, self.money_for_care)
