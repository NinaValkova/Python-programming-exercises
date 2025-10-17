class dictionary_iter:
    def __init__(self, obj):
        self.obj = obj
        self.current = -1

    # iterator is expected to have these two methods:

    # __iter__()   # returns the iterator object itself
    # __next__()   # returns the next value or raises StopIteration

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1

        size = len(self.obj)
        if size == self.current:
            raise StopIteration

        # d.keys() returns a dict_keys view object - dict_keys([1, 2, 3]) - view of the dictionary’s keys.
        key = list(self.obj.keys())[self.current]
        value = self.obj[key]
        return (key, value)

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
