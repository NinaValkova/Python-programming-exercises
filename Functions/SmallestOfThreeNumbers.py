def getSmallest(number_1, number_2, number_3):
    if number_1 < number_2 and number_1 < number_3:
        return number_1
    elif number_2 < number_3:
        return number_2
    
    return number_3
    

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

smallest = getSmallest(number_1, number_2, number_3)
print(smallest)