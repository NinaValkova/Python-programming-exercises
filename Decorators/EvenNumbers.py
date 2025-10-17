# decorator — a function that takes another function as input - function is not data, but code (a callable function)
def even_numbers(function):

    def wrapper(numbers):  #   # accepts the same argument as the decorated function
        current_numbers = function(numbers)  # # call the original function
        even_numbers = []

        for number in current_numbers:
            if number % 2 == 0:
                even_numbers.append(number)

        return even_numbers

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers

print(get_numbers([1, 2, 3, 4, 5]))
