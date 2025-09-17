def getResult(number_1 : int, number_2: int, operator: str):
    result = 0

    match operator:
        case 'multiply':
            result = number_1 * number_2
        case 'divide':
            result = round(number_1 / number_2)
        case 'add':
            result = number_1 + number_2
        case 'subtract':
            result = number_1 - number_2   

    return result                  

operator = input()
number_1 = int(input())
number_2 = int(input())

result = getResult(number_1, number_2, operator)
print(result)