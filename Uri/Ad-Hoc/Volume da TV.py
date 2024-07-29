tv = list(map(int, input().split()))
for x in list(map(int, input().split())):
    tv[0] += x
    if tv[0] < 0:
        tv[0] = 0
    elif tv[0] > 100:
        tv[0] = 100

print(tv[0])