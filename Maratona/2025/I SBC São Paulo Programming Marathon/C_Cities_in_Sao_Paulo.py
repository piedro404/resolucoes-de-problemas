def taDentroDoLimite(x, y):
    if y == 0:
        return -200 <= x <= 200
    
    if y < 0:
        x *= -1
        y *= -1

    return y <= 100 and x+y <= 100 and y - x <= 200

def main():
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        if taDentroDoLimite(x, y):
            print("S")
        else:
            print("N")

main()