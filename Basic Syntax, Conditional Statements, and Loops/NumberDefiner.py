number = float(input())

if(number == 0):
    print("zero")
elif(number > 0):
    if(number > 1_000_000):
        print('large positive')
    elif(number < 1):
        print('small positive')
    else:
        print('positive')
else:
    number = abs(number)
    if(number > 1_000_000):
        print('large negative')
    elif(number < 1):
        print('small negative')
    else:
        print('negative')


