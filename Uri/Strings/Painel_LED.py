def lampandas(lamp, i, n):
    if len(lamp) == i or n == 0:
        return lamp

    if n % 2 != 0:
        lamp[i] = "X" if lamp[i] == "O" else "O"
        if lamp[i] == "X":
            n+=1
    
    lamp = lampandas(lamp, i+1, n//2)

    return lamp 
    
for _ in range(int(input())):
    lamp, trade = map(str, input().split())
    lamp = list(lamp)

    lamp = lampandas(lamp, 0, int(trade))

    print("".join(lamp))