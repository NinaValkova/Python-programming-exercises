class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0
        self.curr_count = -1

    def __iter__(self):
        return self

    def __next__(self):

        if self.curr_count == -1:
            self.curr_count += 1
            return 0

        self.current += self.step
        self.curr_count += 1

        if self.curr_count == self.count:
            raise StopIteration

        return self.current


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
