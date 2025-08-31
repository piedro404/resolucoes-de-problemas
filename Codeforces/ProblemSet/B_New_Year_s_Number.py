def newYear(n):
    while n > 0:
        if n % 2021 == 0 or n % 2020 == 0:
            return "YES"
    
        n -= 2020

    return "NO"


for _ in range(int(input())):
    n = int(input())
    print(newYear(n))
    