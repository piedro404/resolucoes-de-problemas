dbsp = 1000000.00
for _ in range(int(input())):
    g, p = map(float, input().split())
    pC = (g / p)*1000
    if dbsp > pC:
        dbsp = pC

print("{:.2f}".format(dbsp))