def foodLeftDays(C):
    days = 0
    while C > 1: 
        C *= 0.5  
        days += 1
    return f"{days} dias"

for _ in range(int(input())):
    print(foodLeftDays(float(input())))