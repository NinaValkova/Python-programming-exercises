n = int(input())

price = 0
total = 0
for i in range (0,n,1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not (0.01 <= price_per_capsule and  price_per_capsule <= 100.00):
        continue
    if not (1 <= days and days <= 31):
        continue
    if not (1 <= capsules_per_day and capsules_per_day<= 2000):
        continue

    price = price_per_capsule * days * capsules_per_day
    print(f'The price for the coffee is: ${price:.2f}')
    total += price

print(f'Total: ${total:.2f}')