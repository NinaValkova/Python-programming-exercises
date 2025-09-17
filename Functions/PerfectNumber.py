def findDivisors(number):
    divisors = []
    
    for i in range(1, number, 1):
        if number % i == 0:
            divisors.append(i)     
            
    return divisors

def find_sum(divisors):
    sum =0
    
    size = len(divisors)
    for i in range(0, size, 1):
        sum+=divisors[i]
    
    return sum    

number = int(input())

divisors = findDivisors(number)
sum = find_sum(divisors)

if(sum == number):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")    