def fibonacci():
    first = 0
    second = 1

    while True:  # while True creates an infinite loop inside the generator.
                 # Each time you call next(generator), the function resumes where it left off
        if first == 0:
            yield first
        elif second == 1:
            yield second

        sum = first + second
        yield sum

        first, second = second, sum


generator = fibonacci()
for i in range(5):
    print(next(generator))
