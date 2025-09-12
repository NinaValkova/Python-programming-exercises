def areUnique(year : int):
    digits = set()

    digit = 0
    while year > 0:
        digit = year % 10
        if digit in digits:
            return False
        digits.add(digit)
        year//=10

    return True    
        


def findUniqueYear(year : int):
    year += 1 
    while True:
        if areUnique(year):
            return year
        year += 1
        
    return 0     
    

year = int(input())

year_unique_digits = findUniqueYear(year)
print(year_unique_digits)