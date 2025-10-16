class vowels:
    def __init__(self, word):
        self.vowels = ["a", "o", "u", "e", "i", "y"]
        self.word = word
        # instance variable (stored in the object).
        # It remembers where you are in the string across multiple calls to __next__()
        self.current = -1

    def __iter__(self):
        return self

    # __next__() starts from the current value of self.current
    def __next__ (self):
        # Instead of returning nothing, you loop until a vowel is found
        while True:
            self.current += 1
            size = len(self.word)

            if self.current == size:
                raise StopIteration

            letter = self.word[self.current].lower()
            if letter  in self.vowels:
                return self.word[self.current]


my_string = vowels("Abcedifuty0o")
for char in my_string:
    print(char)
