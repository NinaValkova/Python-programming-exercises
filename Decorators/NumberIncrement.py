def number_increment(numbers):

    # inner function can access variables from the outer function
    # Nothing outside number_increment can call increase() directly.
    def increase():
        # # number is a loop variable, a copy of the value in the list
        # for number in numbers:
        #     # Doing number += 1 only changes this local copy, not the list element itself
        #     number += 1
        size = len(numbers)
        for i in range(0, size):
            numbers[i] += 1

        return numbers
        # return [number + 1 for number in numbers] turns a new incremented list.

    return increase()


print(number_increment([1, 2, 3]))
