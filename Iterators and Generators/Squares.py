# generator function 
def squares(n):
        size = n + 1
        for i in range(1, size):
            yield i * i


print(list(squares(5)))
