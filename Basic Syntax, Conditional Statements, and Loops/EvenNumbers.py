n = int(input())

for i in range(0, n, 1):
    number = int(input())

    if(number % 2 == 1):
        # print(number + " is odd!")
        print(f'{number} is odd!')
        break
else:
        print('All numbers are even.')