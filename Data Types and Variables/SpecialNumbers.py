def sumDigits(digit : int):
    sum = 0
    while digit > 0:
        sum += digit % 10
        digit //= 10
        
    if(sum == 5 or sum == 7 or sum == 11):
        return True

    return False

n = int(input())

for i in range(1, n+1, 1):
    if(sumDigits(i)):
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')    

