class Calculator:
    @staticmethod
    def add(*args):
        sum = 0
        for arg in args:
            sum += arg

        return sum

    @staticmethod
    def multiply(*args):
        sum = 1
        for arg in args:
            sum *= arg

        return sum

    @staticmethod
    def divide(*args):
        result = args[0]
        size = len(args)
        for i in range(1, size):
            result = result / args[i]  

        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        size = len(args)
        for i in range(1, size):
            result = result - args[i]  

        return result             


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
