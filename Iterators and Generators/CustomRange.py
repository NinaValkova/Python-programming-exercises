class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start - 1

    # This method is called once, when the iteration starts - give me something I can iterate over
    # object itself to be the iterator.
    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.end:
            raise StopIteration

        return self.current

    # generator knows how to produce the next item each time next() is called — it already implements __next__() internally
    # yield inside __iter__ → creates a generator - it generates items one by one.
    # def __iter__(self):
    #     for num in range(self.start, self.end + 1):
    #         yield num


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
