def solution():

    def integers():
        i = 1
        while True:
            yield i
            i+=1

    def halves():
        for i in integers():
            yield i/2

    def take(n, seq):
        result = []
        count = 0
        for item in seq:
            if count == n:
                break
            result.append(item)
            count += 1
        return result 

    return (take, halves, integers)

take = solution()[0]  # take a reference to the take function - no values are generated yet. Nothing happens until you call the function.
halves = solution()[1]
print(take(5, halves()))
