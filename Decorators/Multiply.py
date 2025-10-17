# is not the decorator itself yet — it’s a decorator factory that creates a decorator
# A function that returns a decorator. Used when you want to pass parameters to your decorator.
def multiply(times):

    # actual decorator - receives the function that you decorate
    # A function that takes another function and returns a new function.
    def decorator(function):

        def wrapper(number):
            current_number = function(number)
            current_number *= times

            return current_number

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))
