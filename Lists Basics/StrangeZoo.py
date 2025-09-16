tail = input()
body = input()
head = input()

result = [tail, body, head]

# temp = result[0]
# result[0] = result[2]
# result[2] = temp

result[0], result[2] = result[2], result[0] #Python evaluates the right-hand side first as a tuple (b, a) and then unpacks it into the variables on the left.

print(result)