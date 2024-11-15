priceTotal = 0
kgTotal = 0
days = int(input())
for x in range(days):
    price = float(input())
    priceTotal += price
    
    kg = len(list(map(str, input().split())))
    kgTotal += kg
    print(f"day {x+1}: {kg} kg")

print(f"{(kgTotal/days):.2f} kg by day")
print(f"R$ {(priceTotal/days):.2f} by day")