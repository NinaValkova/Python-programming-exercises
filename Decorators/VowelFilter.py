def vowel_filter(function):  # Inside vowel_filter, a new function wrapper() is defined.
    vowels = ["a", "o", "u", "e", "i", "y"]

    def wrapper():  # wrapper() calls the original function (function()) to get its output
        letters = function()  # call the original function

        result = []
        for letter in letters:
            if letter in vowels:
                result.append(letter)
        return result

    return wrapper  # vowel_filter returns wrapper, which replaces the original function in build-in function print()


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())


# @decorator
# def some_function(): ...

# is exactly equivalent to:

# def some_function():
#     ...
# some_function = decorator(some_function)
