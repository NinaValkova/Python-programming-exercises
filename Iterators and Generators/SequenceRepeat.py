class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current = -1
        self.curr_count = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        self.curr_count += 1

        size = len(self.sequence)
        if self.curr_count == self.number:
            raise StopIteration
        elif self.current == size:
            self.current = 0

        return self.sequence[self.current]

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
