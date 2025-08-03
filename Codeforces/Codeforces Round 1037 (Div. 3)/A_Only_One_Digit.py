def onlyOndeDigit(n):
    return min(list(str(n)))

for _ in range(int(input())):
    print(onlyOndeDigit(int(input())))